import numpy as np

def eco_simple(song, ganancia, retraso): # ganancia en porcentaje, y retraso en ms

    corrimiento= int(song.fs*retraso*10**-3)      ## retraso en ms
    señal_eco= (ganancia/100)*np.concatenate(np.zeros(corrimiento), song.output_signal)
    song.output_signal = señal_eco + np.concatenate(song.output_signal, np.zeros(corrimiento))



