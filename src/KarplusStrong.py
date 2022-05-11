import numpy as np
from src.NoteClass import Note

class KarplusStrong:
    def __init__(self):
        self.notes = []
        self.instrument = ''
        self.t_len = 0
        self.sample_len = 0
        self.wavetable = []

    def gen_note(self, note, instrument):
        self.t_len = 0
        self.sample_len = 0
        self.wavetable = []
        self.instrument_switch.get(instrument, self.other)(self, note)
        return

    def guitar(self, note):
        self.t_len = int(round(note.fs * note.duration * 1E-6))
        self.sample_len = np.int(note.fs / note.freq)
        self.wavetable = (2 * np.random.randint(0, 2, self.sample_len + 2) - 1).astype(np.float)

        if note.freq < 200E3:       # 20E3
            Y = self.low_freq(0.99)
        elif note.freq > 2E3:
            Y = self.high_freq()
        else:
            Y = self.low_freq(1)

        note.note_signal = Y

        return

    def low_freq(self, ro):
        Y = []
        for i in range(self.t_len):
            if i <= self.sample_len:
                Y.append(ro * (self.wavetable[i] + self.wavetable[i - 1]) / 2)
            else:
                Y.append(ro * (Y[i - self.sample_len] + Y[i - self.sample_len - 1]) / 2)
        return Y

    def high_freq(self):
        Y = []
        for i in range(self.t_len):
            if i <= self.sample_len:
                Y.append((self.wavetable[i] + self.wavetable[i - 1]) / 2)
            else:
                Y.append((Y[i - self.sample_len] + Y[i - self.sample_len - 1]) / 2)
        return Y


    def drums(self, note):
        self.t_len = int(round(note.fs * note.duration * 1E-6))
        self.sample_len = np.int(note.fs / note.freq)
        self.wavetable = (2 * np.random.randint(0, 2, self.sample_len + 2) - 1).astype(np.float)

        Y = []
        for i in range(self.t_len):
            if i <= self.sample_len:
                aux = np.array((self.wavetable[i] + self.wavetable[i - 1]) / 2)
            else:
                aux = np.array((Y[i - self.sample_len] + Y[i - self.sample_len - 1]) / 2)
            r = np.random.randint(2)
            if r == 0:
                Y.append(aux)
            else:
                Y.append(-aux)

        note.note_signal = Y

        return

    def harp(self, note):
        return

    def other(self, note):
        print("qué pusiste rey")

    instrument_switch = {
        'G': guitar,
        'T': drums,
        'H': harp
    }
