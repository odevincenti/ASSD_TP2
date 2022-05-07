from mido import MidiFile
from NoteClass import Note

# from SongClass import Song

########################################################################################################################
# ESTRUCTURA DE UN ARCHIVO MIDI
# - type (int):
#   - 0 Single Track: Tiene 1 sólo track
#   - 1 Synchronous: Todos los tracks empiezan al mismo tiempo
#   - 2 Asynchronous: Cada track es independiente
# - length (float): Tiempo en segundos que dura la canción contenida en el archivo (Sólo para tipos 0 y 1)
# - ticks_per_beat (int): Un beat representa la duración de 1/4 de redonda (1 negra), los beats se dividen en ticks (la
#                         mínima unidad de tiempo en los MIDI). Entonces todas las duraciones de las notas estarán
#                         expresadas en ticks.
#                         Esta variable indica la duración de 1 tick, según cuántos ticks hay en 1 beat
# - tracks (list): Lista de los tracks en formato MidiTrack
#   - MidiTrack (list) : Clase hija de List que contiene los Message
#       - name (string): Nombre del Track
#       - MetaMessage (MetaMessage): Mensaje informativo que representa un evento y que el sintetizador no lee
#           - type (string): Indica el tipo de mensaje ('set_tempo', 'time_signature', 'end_of_track')
#           - Los demás atributos dependerán del tipo de mensaje (https://mido.readthedocs.io/en/latest/meta_message_types.html)
#       - Message (Message): Son las "instrucciones" de la canción. Los atributos dependerán del tipo
#           - type (string): Tipo de instrucción
#               - Note Off (Note, Number,Velocity)
#               - Note On (Note, Number, Velocity)
#               - Polyphonic Aftertouch (Note, Number, Pressure)
#               - Control Change (Controller, Number, Data)
#               - Program Change (Program, Number)
#               - Channel Aftertouch (Pressure)
#               - Pitch Wheel
########################################################################################################################

'''
midi_to_song: Función que extrae la información de un archivo MIDI y la carga en un objeto Song
YA SE QUE TODAVÍA NO LO HACE, ESTOY PROBANDO LA CLASE
'''


def midi_to_song(path):
    midi_types = ["Single Track", "Synchronous", "Asynchronous"]
    mid = MidiFile(path, clip=True)
    print("Archivo:", path.split('\\')[-1])
    print("Tipo:", midi_types[mid.type])
    if mid.type != 2:
        print("Duración:", mid.length / 60, "minutos")
    print("Hay", len(mid.tracks), "tracks")
    return mid

s = midi_to_song(r"C:\Users\odevi\PycharmProjects\ASSD_TP2\midi_samples\RodrigoAdagio.mid")

#C:\Users\odevi\PycharmProjects\ASSD_TP2\midi_samples\RodrigoAdagio.mid

# Recibe un MidiTrack y devuelve un Track (python)
class MIDIHandler:
    def __init__(self, track, ticks_per_beat):
        self.midi_track = track
        self.ticks_per_beat = ticks_per_beat
        self.notes = []
        self.aux_notes = []

        for message in track:
            self.midi_message_switch.get(message.type, self.other)(message)
        return

    def find_note(self, note):
        r = None
        for idn, n in enumerate(self.notes):
            if n.note != note.note:
                pass
            elif n.velocity != note.velocity:
                pass
            else:
                r = idn
                break
        return r

    # note_off(channel, note, velocity)
    def note_off(self, msg):
        print("Note OFF")
        r = True
        idn = self.find_note(msg)
        if idn is not None:
            self.aux_notes[idn].end_time = msg.time
            self.aux_notes[idn].duration = self.aux_notes[idn].end_time - self.aux_notes[idn].start_time
            self.notes.append(self.aux_notes[idn])
            del self.aux_notes[idn]
        else:
            r = False
        return r

    # note_on(channel, note, velocity)
    def note_on(self, msg):
        print("Note ON")
        self.aux_notes.append(Note(msg.note, msg.time, 0, 0, msg.velocity))
        return True

    def set_tempo(self, msg):
        print("Set Tempo")

    def time_signature(self, msg):
        print("Time Signature")

    def end_of_track(self, msg):
        print("End of track")

    def other(self, msg):
        return

    '''# polytouch(channel, note, value)
    def polytouch(self, msg):
        print("Polyphonic Aftertouch")

    # control_change(controller, control, value)
    def control_change(self, mido_message):
        print("Control Change")

    # program_change(channel, program)
    def program_change(self, mido_message):
        print("Program Change")

    # aftertouch(channel, value)
    def aftertouch(self, mido_message):
        print("Channel Aftertouch")

    # pitchwheel(channel, pitch)
    def pitchwheel(self, mido_message):
        print("Pitch Wheel")'''

    # todo: Completar lista: https://mido.readthedocs.io/en/latest/message_types.html
    midi_message_switch = {
        0: note_off,
        1: note_on,
        2: set_tempo,
        3: time_signature,
        4: end_of_track,
    }
