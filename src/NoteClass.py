import numpy as np


class Note:
    def __init__(self, freq, start_time, duration, end_time, velocity, fs):
        self.freq = freq
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

