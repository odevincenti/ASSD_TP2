import pandas as pd
from src.NoteClass import Note

#Con esta clase vamos a manejar las parciales de cada un insturmento
class Partial(Note):
    def __init__(self, freq, start_time, duration, end_time, velocity):
        super().__init__(freq, start_time, duration, end_time, velocity)
        #self.ADSR = ADSR   #Vector con componentes [attack_time , decay_time , sustain_time , release_time ]

class ProcessedNote:
    def __init__(self):
        self.frecuencia = None
        self.fase = None
        self.ADSR = None
        self.instrumento = None
        self.nota = None
        self.PartialNote = []  #Arreglo de las parciales individuales (forma de notas)

    def create_partial(self, path_a_data, instrumento, frecuencia):
        #Funcion que lee el txt con la tabla de informacion de los partials de una nota de un instrumento
        # path_a_data: Path al txt
        # instrumento = indice que indica el insturmento (por ahora solo flauta)
        # frecuencia = frecuencia de la nota que queremos sintetizar
        ##############################################################################################################

        PartialsFile = pd.read_csv(path_a_data, sep='\t')  #Archivo con los componentes parciales de una nota
        print(PartialsFile)
        column = PartialsFile["Amplitud"]
        frecuencia_samples_ix = column.idxmax()
        frecuencia_samples = PartialsFile["Frecuencia"][frecuencia_samples_ix]   #Obtengo la frecuencia principal de la muestra

        for k in range(0,len(PartialsFile)):
            multiplier = frecuencia/frecuencia_samples   #Multiplicador para pasar la nota a diferentes octavas
            frec = PartialsFile["Frecuencia"][k] * multiplier
            ampli = PartialsFile["Amplitud"][k]
            fase = PartialsFile["Fase"][k]

            print(frec,ampli,fase)

        #self.PartialNote.append()