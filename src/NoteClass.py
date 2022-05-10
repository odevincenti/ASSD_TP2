import numpy as np

class Note:
    def __init__(self, note, start_time, duration, end_time, velocity, fs=100E3):
        self.note = note
        self.freq = self.note2freq(note)
        self.start_time = start_time            # Tiempo en microsegundos
        self.duration = duration                # Tiempo de microsegundos
        self.end_time = end_time                # Tiempo de microsegundos
        self.velocity = velocity
        self.note_signal = None
        self.fs = fs
        self.time_base = np.linspace(self.start_time, self.end_time, int(self.fs * self.duration*1E-6))

    def set_note_signal(self, note_signal):
        self.note_signal = note_signal

    def update_fs(self, fs):
        self.fs = fs
        self.time_base = np.linspace(self.start_time, self.end_time, self.fs * self.duration)

    def create_time_base(self):
        self.time_base = np.linspace(self.start_time, self.end_time, self.fs * self.duration)

    def note2freq(self, note):
        return 8.1757989156 * (2 ** (note / 12))
