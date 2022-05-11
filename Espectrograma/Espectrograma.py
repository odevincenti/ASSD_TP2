from scipy import signal as sign
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from signal import signal


def Espectro(x, nfft_, f_s, window_, n_per_seg, overlap):


    f, t, S = sign.spectrogram(x, fs=f_s, window=window_, nfft=nfft_,nperseg=n_per_seg, noverlap=overlap)

    #plt.specgram(x, fs=f_s, window=window_, nperseg=n_per_seg, noverlap=overlap, cmap='jet_r')
    plt.colorbar()
    plt.pcolormesh(t, f, 10*np.log10(S))
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.title("Espectrograma")
    plt.show()


if __name__ == "__main__":
    nfft = None
    f_s, x = wavfile.read('Sol_Mayor.wav')
    window = 'bartlett'
    n_per_seg = None
    overlap = 50

    #windows: ["boxcar", "triang", "blackman", "hamming", "hann", "bartlett", "flattop", "parzen", "bohman", "blackmanharris", "nuttall", "barthann"]
    Espectro(x, nfft, f_s, window, n_per_seg, overlap)
