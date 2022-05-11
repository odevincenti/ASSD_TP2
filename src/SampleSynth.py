import numpy as np
import os

class SampleSynth:
    def __init__(self):
        self.instrument = ''
        self.samples_directory = ""
        self.samples_diccionario = {}
        self.creo_my_diccionario()


    def gen_note(self,note,instrumento):
        # Proceso los samples del instrumento que quiero a partir de la carpeta samples/instrumento
        self.proceso_samples(instrumento)

        # Me llega una nota y busco en mis muestras cual es la nota mas cercana a es que tengo
        # note.freq es el codigo midi de la nota
        Nota_string = min(self.samples_diccionario, key = lambda v: abs(self.samples_diccionario[v] - note.freq))



    def proceso_samples(self, instrumento):
        #Creo un diccionario de la forma: [nota , frecuencia]
        self.samples_directory = "../Samples/" + instrumento + "/"

        for sample in os.listdir(self.samples_directory):
            nota_file = sample.split(".")
            print(nota_file[0])

            self.samples_diccionario[sample] = self.Notas_que_hay_en_sample[nota_file[0]]
            # ej forma de diccionario:
            # {'C3.wav': 130.813,
            #  'C4.wav': 261.626,
            #  'C5.wav': 523.251}

    def creo_my_diccionario(self):
        self.Notas_que_hay_en_sample = {}
        NOTAS = ["A0", "Bb0", "B0",
                       "C1", "Db1", "D1", "Eb1", "E1", "F1", "Gb1", "G1", "Ab1", "A1", "Bb1", "B1",
                       "C2", "Db2", "D2", "Eb2", "E2", "F2", "Gb2", "G2", "Ab2", "A2", "Bb2", "B2",
                       "C3", "Db3", "D3", "Eb3", "E3", "F3", "Gb3", "G3", "Ab3", "A3", "Bb3", "B3",
                       "C4", "Db4", "D4", "Eb4", "E4", "F4", "Gb4", "G4", "Ab4", "A4", "Bb4", "B4",
                       "C5", "Db5", "D5", "Eb5", "E5", "F5", "Gb5", "G5", "Ab5", "A5", "Bb5", "B5",
                       "C6", "Db6", "D6", "Eb6", "E6", "F6", "Gb6", "G6", "Ab6", "A6", "Bb6", "B6",
                       "C7", "Db7", "D7", "Eb7", "E7", "F7", "Gb7", "G7", "Ab7", "A7", "Bb7", "B7",
                       "C8"]
        i = 0
        for note in NOTAS:
            prev_freq = round(440 / 32 * (2 ** (((21 + i) - 9) / 12)), 3)
            self.Notas_que_hay_en_sample[note] = prev_freq
            i += 1