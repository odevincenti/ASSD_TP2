from mido import MidiFile
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
        print("Duración:", mid.length/60, "minutos")
    print("Hay", len(mid.tracks), "tracks")
    for i in range(len(mid.tracks)):
        print("Track", i, ":", len(mid.tracks[i]), "Messages")
    return mid

s = midi_to_song(r"C:\Users\odevi\PycharmProjects\ASSD_TP2\midi_samples\RodrigoAdagio.mid")
