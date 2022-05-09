import numpy as np
import time

################################################    PARTIAL NOTE    ################################################

# La clase partial note se va a encargar de procesar cada uno de los
# parciales de cada nota

####################################################################################################################


class PartialNote:


    ########################    INIT    ########################
    def __init__(self, amplitud, freq, phase, start_time, D_time, D_amp, S_time, S_amp, R_time, R_amp, off_time):

        # A la funcion __init__ se la para configurar cada uno de los parciales correspondientes a la nota

        # Dicha clase utilizara las siguientes variables

        #   freq: Frecuencia del parcial.
        #   phase: Fase del sample a la frecuencia del parcial.

        #   start_time: Tiempo en el cual comienza la nota.

        #   D_time: Tiempo en el que termina el attack y comienza el decay
        #   D_amp: Amplitud alcanzada en el punto entre las etapas de attack y decay.

        #   S_time: Tiempo en el que termina el decay y comienza el sustain
        #   S_amp: Amplitud alcanzada en el punto entre las etapas de decay y sustain.

        #   R_time: Tiempo en el que termina el sustain y comienza el release
        #   R_amp: Amplitud alcanzada en el punto entre las etapas de sustain y release.

        #   off_time: Tiempo en el que se observa que la señal se anula. Fin de la etapa de release


        #       /\
        #      /  \                             0: start_time
        #     /    \_________                   1: D_time
        #    /               \                  2: S_time
        #   /                 \                 3: R_time
        #  /----+--+-------+---\---> t          4: off_time
        #  0    1  2       3   4
        #     A   D    S      R



        self.freq = freq
        self.phase = phase
        self.ampli = amplitud

        #Todos los tiempos son medidos desde el inicio
        # Tiempo de inicio
        self.start_time = start_time

        # Tiempo de inicio hasta Tiempo de D
        self.D_time = D_time - start_time
        self.D_amp = D_amp

        # Tiempo de inicio hasta tiempo de S
        self.S_time = S_time - start_time
        self.S_amp = S_amp

        # Tiempo de  inicio hasta tiempo de R
        self.R_time = R_time - start_time
        self.R_amp = R_amp

        # Tiempo desde el inicio hasta el fin de la etapa de release.
        self.off_time = off_time - start_time


       # Preparo las pendientes
        self.release_time = self.R_time
        self.A_pendiente = self.D_amp / self.D_time                                 # Pendiente de la etapa de attack.
        self.D_pendiente = (self.S_amp - self.D_amp) / (self.S_time - self.D_time)  # Pendiente de la etapa de decay.
        self.S_pendiente = (self.R_amp - self.S_amp) / (self.R_time - self.S_time)  # Pendiente de la etapa de sustain.
        self.R_pendiente = (- self.R_amp) / (self.off_time - self.R_time)           # Pendiente de la etapa de release.

        self.output_signal = np.array([])  # ADSR del parcial pedido

        self.final_ASDR_time = -1  # Tiempo en el cual la ADSR del parcial se hará 0.

    ########################    GETTERS     ########################
    def get_phase(self):
        return self.phase

    def get_freq(self):
        return self.freq

    def get_ampli(self):
        return self.ampli

    def get_final_ASDR_time(self, note):

        # Si se completan las etapas de attack y decay
        if (note.duration >= self.S_time):

            # Si la pendiente de sustain es positiva o la duracion es menor que el tiempo en que la etapa S se haria 0.
            # ==> El tiempo maximo es cuando la etapa R se hace 0.
            if ((self.S_pendiente >= 0) or note.duration <= self.S_time - self.S_amp / self.S_pendiente):
                return note.duration - ((note.duration - self.S_time) * self.S_pendiente + self.S_amp) / self.R_pendiente

            # Si no se llega a la etapa R antes de que se anule S
            # ==> El timepo maximo es cuando se anula S
            else:
                return self.S_time - self.S_amp / self.S_pendiente


        # Si no se completan todas las etapas
        else:

            # Si no se completan todas las etapas y no hay etapa D
            if note.duration <= self.D_time:
                return note.duration - ((note.duration) * self.A_pendiente) / self.R_pendiente

            # Si no se completan todas las etapas y no hay etapa S
            elif note.duration <= self.S_time:
                return note.duration - ((note.duration - self.D_time) * self.D_pendiente + self.D_amp) / self.R_pendiente

    def get_amplitude_array(self, note):

        # Se obtiene la ADSR del parcial y lo guarda en self.output_signal

        final_ASDR_time = self.get_final_ASDR_time(note)  # Guardo el tiempo en el cual la ADSR del parcial se hará 0.
        self.final_ASDR_time = final_ASDR_time

        data = self.get_adsr(note, final_ASDR_time)

        self.output_signal = data

    def get_adsr(self, note, final_ASDR_time):

        ###################################################################
        # QUE ES UN ADSR? (Envolvente: Variación de la intensidad sonora)

        #  Un sonido que se reproduce está condicionado a sufrir alteraciones durante su evolución
        #  temporal a través del tiempo. La envolvente lo que hace es segmentar e intervenir en cada
        #  una de las partes durante la evolución temporal del sonido, desde su inicio hasta su final.

        # Arreglo de valores (depende de final_ASDR_time)
        note_out = np.linspace(0, final_ASDR_time, int(final_ASDR_time * note.fs))

        R_time_index = int(round(note.duration * note.fs))

        # Si la duracion de la nota es mas grande que el tiempo total de las 4 etadpas
        if (note.duration >= self.S_time):

            D_time_index = int(round((self.D_time) * note.fs))
            S_time_index = int(round((self.S_time) * note.fs))

            #Se divide el arreglo en las etapas
            stageA, stageD, stageS, stageR = np.split(note_out, [D_time_index, S_time_index, R_time_index])

            # Se calculan las etapas de la ADSR.
            stageA = (stageA) * self.A_pendiente
            stageD = (stageD - self.D_time) * self.D_pendiente + self.D_amp
            stageS = (stageS - self.S_time) * self.S_pendiente + self.S_amp
            stageR = (stageR - note.duration) * self.R_pendiente + ( note.duration - self.S_time) * self.S_pendiente + self.S_amp

            data = np.concatenate([stageA, stageD, stageS, stageR])  # Se concatenan las etapas

        # Si no se completan todas las etapas...
        else:
            # Etapas AR
            if note.duration <= self.D_time:
                stageA, stageR = np.split(note_out, [R_time_index])
                stageA = (stageA) * self.A_pendiente
                stageR = (stageR - note.duration) * self.R_pendiente + note.duration * self.A_pendiente
                data = np.concatenate([stageA, stageR])


            # Etapas A D y R
            elif note.duration <= self.S_time:
                D_time_index = int(round((self.D_time) * note.fs))
                stageA, stageD, stageR = np.split(note_out, [D_time_index, R_time_index])
                stageA = (stageA) * self.A_pendiente
                stageD = self.D_amp + self.D_pendiente * (stageD - self.D_time)
                stageR = (stageR - note.duration) * self.R_pendiente + self.D_amp + ( note.duration - self.D_time) * self.D_pendiente
                data = np.concatenate([stageA, stageD, stageR])  # Se concatenan las etapas

        return data
