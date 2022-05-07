from mido import MidiFile
from midi_handler import midi_message_switch

class Song:
    def __init__(self):
        self.midi = None
        self.tracks = None
        self.fs = 0.0
        self.duration = 0.0
        self.time_base = 0.0
        self.output_signal = None

    def set_output_signal(self, output_signal):
        self.output_signal = output_signal

    def set_midi(self, path):
        self.midi = MidiFile(path, clip=True)
        for track in self.midi.tracks:
            name = track.name
            for message in track:
                note = midi_message_switch.get(message.type)()


