
class Song:
    def __init__(self):
        self.midi_file = None
        self.tracks = None
        self.fs = 0.0
        self.duration = 0.0
        self.time_base = 0.0
        self.output_signal = None

    def set_output_signal(self, output_signal):
        self.output_signal = output_signal
