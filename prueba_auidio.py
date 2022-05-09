import numpy as np
import pyaudio
import simpleaudio as sa
f=5000
fs=44100
t = np.linspace(0,3, 3*fs)
signal= np.sin(2*np.pi*t*f) + np.sin(2*np.pi*t*(f+8000))
signal *= 32767 / np.max(np.abs(signal))
signal = signal.astype(np.int16)
play = sa.play_buffer(signal, 1,2, fs)
play.wait_done()

