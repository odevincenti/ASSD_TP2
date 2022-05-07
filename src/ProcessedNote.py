import pandas as pd
from src.NoteClass import Note

#Con esta clase vamos a manejar las parciales de cada un insturmento
class Partial(Note):
    def __init__(self, freq, start_time, duration, end_time, velocity):
        super().__init__(freq, start_time, duration, end_time, velocity)

class ProcessedNote:
    def __init__(self):
        self.frecuencia = None
        self.fase = None
        self.ADSR = None
        self.instrumento = None
        self.nota = None
        self.PartialNote = []  #Arreglo de las parciales individuales (forma de notas)

    def create_partial(self, path_a_data, instrumento):
        #Funcion que lee el txt con la tabla de informacion de los partials de un instrumento
        #Leemos ese txt y llenamos la tabla de parciales Partial
        filee = pd.read_csv(path_a_data, sep='\t')
        #self.PartialNote.append()