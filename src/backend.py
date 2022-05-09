import numpy as np

from SongClass import Song

import pyaudio
import sounddevice as sa

from scipy.io import wavfile



def note2freq(note):
    return 8.1757989156 * (2 ** (note / 12))


class backend():

    def __init__(self):
        self.song = Song()
        #self.additive = Additive()

    def synthesize_song(self):
        self.song.output_signal = []
        for i in range(len(self.song.tracks)):
            if self.song.tracks[i].activate:
                self.synthesize_track(self.song.tracks[i])
            else:
                self.song.tracks[i].signal_out = []
            self.song.output_signal += self.song.tracks[i].signal_out

    def synthesize_track(self, track):
        if track.change == 1:
            track.signal_out=[]
            for i in range(len(track.notes)):
                self.synthesize_note(track.notes[i], self.track.instrument)
                if  track.notes[i].start_time != 0:
                    diference = track.notes[i].start_time*track.notes[i].fs
                    track.notes[i].note_signal = np.concatenate(np.zeros(diference), self.track.notes[i].note_signal)
                if  track.notes[i].end_time != self.song.duration:
                    diferencef = (self.song.duration-track.notes[i].end_time)*self.song.fs
                    track.notes[i].note_signal = np.concatenate(track.notes[i].note_signal, np.zeros(diferencef))
                track.signal_out += track.notes[i].note_signal

    def synthesize_note(self, note, instrument):
        print("xd")
        # llamar a create_note(self, note, instrument)
            # metodo: A - Additive
            #         K - Karpulus Strong
            # En un futuro no muy lejano create_note recibe un parámetro metodo que diga cual metodo de sintetizar usa


    # Suma las señales de track tomando en cuenta el tiempo que dura cada uno y formando la cancion entera

    def output_signal_song(self):
        print("xddd")

    def play_signal(self, signal):
        signal *= 32767 / np.max(np.abs(signal))
        signal = signal.astype(np.int16)
        self.play = sa.play_buffer(signal, 1, 2, self.song.fs)
    ### Interfaz con el back

    # una vez que desde el front se modifico la clase Song , llamando a track.update si es el mismo path anterior
    # para sintetizar la cancion

    def quantity_of_tracks(self):
        return len(self.song.tracks)

    def update_path(self, path):
        if self.song.midi != path:
            self.song.set_midi(path)

    def process_song(self):
        if self.song is not None:
            self.syntethize_song()

    def update_track(self, number_track, instrument, activate, velocity):
        if number_track < len(self.song.tracks):
            self.song.tracks[number_track].update(velocity, activate, instrument)
            return True
        else:
            return False

    def play_song(self):
        if self.song.output_signal is not None:
            self.play_signal(self.song.output_signal)

    def play_track(self, n_track):
        if self.song is not None:
            if n_track < len(self.song.tracks):
                self.synthesize_track(self.song.tracks[n_track])
                self.play_signal(self.song.tracks[n_track].signal_out)
            else:
                return -1
        return -1

    def pause_reproduction(self):
        if (self.play.isplaying()) and (self.play is not None):
            self.play.stop()
        else:
            return -1

    def save_wav_file(self, filename):
        signal = self.song.output_signal(32767 / np.max(np.abs(self.song.output_signal)))
        signal = signal.astype(np.int16)
        wavfile.write(filename, self.song.fs,signal)