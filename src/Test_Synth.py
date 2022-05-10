from src.ProcessedNote import ProcessedNote
from src.NoteClass import Note
import matplotlib.pyplot as plot

note = 59
start_time = 4133521.625
end_time = 5454544.0
duration = 1321022.375
freq = 245.94165062674196
velocity = 95
fs = 10000
nota = Note(note, start_time, duration, end_time, velocity, fs)

Synth = ProcessedNote()

Synth.create_note(nota, "F")

time = nota.create_time_base()

plot.plot(time, nota.note_signal)
