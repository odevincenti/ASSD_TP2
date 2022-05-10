import pandas as pd
import numpy as np
from src.Partials import PartialNote
import os


class ProcessedNote:
    def __init__(self):
        self.frecuencia = None
        self.fase = None
        self.ADSR = None
        self.instrumento = None
        self.nota = None
        self.PartialNotes = []  #Arreglo de las parciales individuales (forma de notas)

    def create_note(self, note, instrument):
        # En objeto note tengo que llenar self.node_signal solo el eje y.
        # Para el tiempo usas self.time_base. Previamente llamar a funcion de la clase create_time_base(self)
        # El instrumento te define el metodo pq hicimos un instrumento por metodo
        # note: Clase note
        #          self.note = note
        #          self.freq = self.note2freq(note)
        #          self.start_time = start_time  # Tiempo en microsegundos
        #          self.duration = duration  # Tiempo de microsegundos
        #          self.end_time = end_time  # Tiempo de microsegundos
        #          self.velocity = velocity
        #          self.note_signal = None
        #          self.fs = fs
        #          self.time_base = []
        #
        # instrument: F: flauta --> Additive
        #             P: piano  --> Karpulus
        ################################################################################################################
        # Crear la señal de salida (self.note_signal) del objeto nota que ingrese como parametro
        amplitude_array = None
     #   note.create_time_base()

        #ADDITIVE SYNTHESIS#######################################################################################
        if instrument == 'F':
            self.create_partial(note.note,"Flauta",note.freq)

            # Para cada parcial...
            for i in range(0, len(self.PartialNotes)):

                freq = self.PartialNotes[i].get_freq()
                phase = self.PartialNotes[i].get_phase()
                ampli_partial = self.PartialNotes[i].get_ampli()

                # Obtengo el ADSR del parcial
                self.PartialNotes[i].get_amplitude_array(note)

                #Un arreglo que va de cero a el tiempo maximo del parcial
                time_vals = note.time_base
                print("\n TAMAÑO TIME BASE: ",np.size(time_vals),"\n")
                print("\n TAMAÑO DE UN PARTIAL:" , np.size(self.PartialNotes[i].output_signal),"\n")

                #Multiplico la ADSR con el seno de cada parcial
                output_sine = ampli_partial * self.PartialNotes[i].output_signal * np.sin(freq * 2 * np.pi * time_vals - 180 * phase / np.pi)
                print("\n TAMAÑO OUTPUT SINE: ", np.size(output_sine) ,"\n")

                self.PartialNotes[i].output_signal = None  # Libero la memoria

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

            note.set_note_signal(amplitude_array)


        #KARPUTULS STRONG############################################################################################
        elif instrument == 'P':
            print("En un futuro tendremos karpulus yo lo se")


    def create_partial(self, midi_note , instrument, frecuencia):
    # Funcion que lee el txt con la tabla de informacion de los partials de una nota de un instrumento
    # int    midinote:     numero midi que indica una nota. la parseamos para convertir a DO RE MI FA SOL LA SI
    # string instrumento:  indice que indica el insturmento (por ahora solo flauta)
    # string frecuencia:   frecuencia de la nota que queremos sintetizar
    ##############################################################################################################
        NOTA = self.convert_midinote(midi_note)

        #########################
        #      IMPORTANTE!      # ======> # LA VARIABLE NOTA TIENE QUE IR EN MAYUSCULA Y ES UN STRING!
        #      IMPORTANTE!      # ======> # la variable instrumento va en minuscula y es un string
        #########################

        #Primero preparo el path de la nota segun el instrumento
        # path_a_data: Path al txt ( Ejemplo: "../MATLAB/Parciales_txts/Flauta/Parciales_DO.txt" )

        path_a_data = "../MATLAB/Parciales_txts/" + instrument + "/Parciales_" + NOTA + ".txt"


        note_partials_file = pd.read_csv(path_a_data, sep='\t')  #Archivo con los componentes parciales de una nota
        print(note_partials_file)

        column = note_partials_file["Amplitud"]
        frecuencia_samples_ix = column.idxmax()
        frecuencia_samples = note_partials_file["Frecuencia"][frecuencia_samples_ix]   #Obtengo la frecuencia principal de la muestra
        multiplier = frecuencia / frecuencia_samples  # Multiplicador para pasar la nota a diferentes octavas

        for k in range(0,len(note_partials_file)):
            frec =          note_partials_file["Frecuencia"][k] * multiplier
            ampli =         note_partials_file["Amplitud"][k]
            fase =          note_partials_file["Fase"][k]
            start_time =    note_partials_file["Start_time"][k]
            D_time =        note_partials_file["D_time"][k]
            D_amp =         note_partials_file["D_amp"][k]
            S_time =        note_partials_file["S_time"][k]
            S_amp =         note_partials_file["S_amp"][k]
            R_time =        note_partials_file["R_time"][k]
            R_amp =         note_partials_file["R_amp"][k]
            off_time =      note_partials_file["Off_time"][k]

            #Con toda esta info creamos la informacion de cada parcial que compone a una nota
            partial_aux = PartialNote(ampli,frec,fase,start_time,D_time,D_amp,S_time,S_amp,R_time,R_amp,off_time)
            self.PartialNotes.append(partial_aux)


    def convert_midinote(self , midi_note):
        note_str = ['DO', 'DO', 'RE', 'RE', 'MI', 'FA', 'FA', 'SOL', 'SOL', 'LA', 'LA', 'SI']
        note_id = midi_note % 12

        print("\n CONVERT MIDI NOTE \nMidinote % 12 :" , note_str[note_id])
        return note_str[note_id]
