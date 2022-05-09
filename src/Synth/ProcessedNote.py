import pandas as pd
import numpy as np
from Partial import PartialNote


class ProcessedNote:
    def __init__(self):
        self.frecuencia = None
        self.fase = None
        self.ADSR = None
        self.instrumento = None
        self.nota = None
        self.PartialNote = []  #Arreglo de las parciales individuales (forma de notas)

    def create_partial(self, instrumento, frecuencia, NOTA):
        # Funcion que lee el txt con la tabla de informacion de los partials de una nota de un instrumento

        #########################
        #       IMPORTANTE!     # ======> # LA VARIABLE NOTA TIENE QUE IR EN MAYUSCULA!
        #########################


        #Primero preparo el path de la nota segun el instrumento
        # path_a_data: Path al txt ( Ejemplo: "./MATLAB/Parciales_txts/Flauta/Parciales_DO.txt" )
        path_a_data = "./MATLAB/Parciales_txts/" + instrumento + "/Parciales_" + NOTA + ".txt"

        PartialsFile = pd.read_csv(path_a_data, sep='\t')  #Archivo con los componentes parciales de una nota
        #print(PartialsFile)

        column = PartialsFile["Amplitud"]
        frecuencia_samples_ix = column.idxmax()
        frecuencia_samples = PartialsFile["Frecuencia"][frecuencia_samples_ix]   #Obtengo la frecuencia principal de la muestra

        for k in range(0,len(PartialsFile)):
            multiplier = frecuencia/frecuencia_samples   #Multiplicador para pasar la nota a diferentes octavas
            frec =          PartialsFile["Frecuencia"][k] * multiplier
            ampli =         PartialsFile["Amplitud"][k]
            fase =          PartialsFile["Fase"][k]
            start_time =    PartialsFile["Start_time"][k]
            D_time =        PartialsFile["D_time"][k]
            D_amp =         PartialsFile["D_amp"][k]
            S_time =        PartialsFile["S_time"][k]
            S_amp =         PartialsFile["S_amp"][k]
            R_time =        PartialsFile["R_time"][k]
            R_amp =         PartialsFile["R_amp"][k]
            off_time =      PartialsFile["Off_time"][k]

            partial_aux = PartialNote(frec,fase,start_time,D_time,D_amp,S_time,S_amp,R_time,R_amp,off_time)
            self.PartialNote.append(partial_aux)




    def create_note_of(self, instruent, note):

        # Crear la señal de salida de la nota que ingrese como parametro
        amplitude_array = None

        # Obtengo los parciales de la nota, segun el instrumento
        #REVISAR LLAMADO
        self.create_partial(instruent,600,"DO")


        # Para cada parcial...
        for i in range(0, len(self.PartialNote)):

            freq = self.PartialNote[i].get_freq()
            phase = self.PartialNote[i].get_phase()

            # Obtengo el ADSR del parcial
            self.PartialNote[i].get_amplitude_array(note)

            #Un arreglo que va de cero a el tiempo maximo del parcial
            time_vals = np.linspace(0, self.PartialNote[i].final_ASDR_time, int(note.fs * self.PartialNote[i].final_ASDR_time))

            #Multiplico la ADSR con el seno de cada parcial
            output_sine = self.PartialNote[i].output_signal * np.sin(freq * 2 * np.pi * time_vals - 180 * phase / np.pi)

            self.PartialNote[i].output_signal = None  # Libero la memoria

            # Se suman las señales de cada parcial
            if i == 0:
                amplitude_array = output_sine
            else:
                difference = len(amplitude_array) - len(output_sine)    # Chequea diferencias de longitudes para poder sumar
                zeros = np.zeros(abs(difference))                       # Crea un arreglo de ceros que permita igualar las longitudes
                if (difference > 0):                                    # Dependiendo de cual sea mas grande, el arreglo de ceros se concatena a uno u otros
                    amplitude_array += np.concatenate([output_sine, zeros])  # Se concatena y se suma

                elif (difference < 0):
                    amplitude_array = np.concatenate([amplitude_array, zeros]) + output_sine

                else:
                    amplitude_array += output_sine

        note.output_signal = amplitude_array

