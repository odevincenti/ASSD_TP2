
class Note:
    def __init__(self, freq, start_time, duration, end_time, velocity):
        self.freq = freq
        self.start_time = start_time
        self.duration = duration
        self.end_time = end_time
        self.velocity = velocity
        self.note_signal = None

    def set_note_signal(self, note_signal):
        self.note_signal = note_signal

