import numpy as np

from SongClass import Song
from midi_handler import midi_to_song
import pyaudio
import sounddevice as sd



def note2freq(note):
    return 8.1757989156 * (2 ** (note / 12))


class backend():

    def __init__(self):
        self.song= Song()
        #self.additive = Additive()

    # una vez que desde el front se modifico la clase Song , llamando a track.update si es el mismo path anterior
    # para sintetizar la cancion
    def update(self, path):
        if(self.song.midi != path)
            self.song = midi_to_song(path)
        self.syntethize_song()

    def synthesize_song(self):
        self.song.output_signal=[]
        for i in range(len(self.song.tracks)):
            if(self.song.tracks[i].activate)
                self.song.tracks[i].signal_out = self.synthesize_track(self.song.tracks[i])
            else:
                self.song.tracks[i].signal_out = []
            self.song.output_signal += self.song.tracks[i].signal_out

    def synthesize_track(self, track ):
        if(track.change == 1)
            self.track.signal_out=[]
            for i in range(len(self.track.notes)):
                self.track.notes[i].note_signal=self.synthesize_note(self.track.notes[i], self.track.instrument)
                if ( self.track.notes[i].start_time != 0)
                    diference = self.track.notes[i].start_time*self.track.notes[i].fs
                    self.track.notes[i].note_signal = np.concatenate(np.zeros(diference),self.track.notes[i].note_signal)
                if ( self.track.notes[i].end_time != self.song.duration)
                    diferencef = (self.song.duration-self.track.notes[i].end_time)*self.song.fs
                    self.track.notes[i].note_signal = np.concatenate(self.track.notes[i].note_signal, np.zeros(diferencef))
                self.track.signal_out += self.track.notes[i].note_signal


    def synthesize_note(self, note, instrument):
        ## llama a additive o el sintetizador a usar
    # Suma las señales de track tomando en cuenta el tiempo que dura cada uno y formando la cancion entera
    def output_signal_song(self)

    def start_playing_signal(self, signal):

        signal *= 32767 / np.max(np.abs(signal))

        tape = tape.astype(np.int16)

        play = sa.play_buffer(tape, 1, 2, smpl_rate)


    def assign_intrument_to_track(self, track_number, instrument, volume, activate):
        if(track_number < len(self.song.tracks)):
            self.song.tracks[track_number].instrument = instrument
            self.song.tracks[track_number].velocity = volume
            self.song.tracks[track_number].activate = activate