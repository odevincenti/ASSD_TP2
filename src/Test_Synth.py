from src.ProcessedNote import ProcessedNote
from src.NoteClass import Note
import numpy as np
import simpleaudio as sa
import matplotlib.pyplot as plot


#####################    NOTAS   ########################
#          Sea k perteneciente a los numeros enteros
#  DO  - 12 * k || 13 * k   k > 5
#  RE  - 14 * k || 15 * k   k > 4
#  MI  - 16 * k             k > 3
#  FA  - 17 * k || 18 * k   k > 3
#  SOL - 31 * k || 32 * k   k > 2
#  LA  - 33 * k || 34 * k   k > 2
#  SI  - 35 * k
#########################################################
# Suenan bien las notas notas de 36 a 83

note = 130
start_time = 4133521.625
end_time = 5454544.0
duration = 1321022.375
freq = 100
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

