from src.ProcessedNote import ProcessedNote
from src.NoteClass import Note
import matplotlib.pyplot as plot

note = 59
start_time = 4133521.625
end_time = 5454544.0
duration = 1321022.375
fs = 0
freq = 245.94165062674196
velocity = 95

nota = Note(note, start_time, duration, end_time, velocity, fs)

ProcessedNote.create_note(nota.note, 'F')

time = nota.create_time_base()

plot.plot(time, nota.note_signal)
