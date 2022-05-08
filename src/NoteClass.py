import numpy as np

class Note:
    def __init__(self, note, start_time, duration, end_time, velocity, fs=0):
        self.note = note
        self.freq = self.note2freq(note)
        self.start_time = start_time
        self.duration = duration
        self.end_time = end_time
        self.velocity = velocity
        self.note_signal = None
        self.fs = fs
        self.time_base = []

    def set_note_signal(self, note_signal):
        self.note_signal = note_signal

    def create_time_base(self):
        self.time_base = np.linspace(self.start_time, self.end_time, self.fs * self.duration)

    def note2freq(self, note):
        return 8.1757989156 * (2 ** (note / 12))
