from src.ProcessedNote import ProcessedNote
from src.NoteClass import Note
import numpy as np
import simpleaudio as sa
import matplotlib.pyplot as plot

note = 59  # SI
start_time = 4133521.625
end_time = 5454544.0
duration = 1321022.375
freq = 500
#freq = 245.94165062674196
velocity = 95
fs = 44100

nota = Note(note, start_time, duration, end_time, velocity, fs)

Synth = ProcessedNote()

Synth.create_note(nota, "F")


print(np.size(nota.time_base))
print(np.size(nota.note_signal))

plot.plot(nota.time_base, nota.note_signal)
plot.show()

signal = nota.note_signal
signal *= 32767 / np.max(np.abs(nota.note_signal))
signal = signal.astype(np.int16)

play = sa.play_buffer(signal, 1 ,2, fs)
play.wait_done()

