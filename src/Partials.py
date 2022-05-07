import pandas as pd

#Con esta clase vamos a manejar las parciales de cada un insturmento

class Partials:
    def __init__(self):
        self.frecuencia = None
        self.fase = None
        self.ADSR = None
        self.instrumento = None
        self.nota = None
        self.PartialNote = None   #Arreglo de las parciales individuales

    def create_partial(self, path_a_data, instrumento):
        #Funcion que lee el txt con la tabla de informacion de los partials de un instrumento
        #Leemos ese txt y llenamos la tabla de parciales Partial
        filee = pd.read_csv(path_a_data, sep='\t')

        print(filee)