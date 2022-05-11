import numpy as np
import soundfile
import os
import librosa

class SampleSynth:
    def __init__(self):
        self.instrument = ''
        self.samples_directorio = ""
        self.samples_diccionario = {}
        self.creo_my_diccionario()


    def gen_note(self,note,instrumento):
        # Proceso los samples del instrumento que quiero a partir de la carpeta samples/instrumento
        self.proceso_samples(instrumento)

        # Me llega una nota y busco en mis muestras cual es la nota mas cercana a es que tengo
        # note.freq es el codigo midi de la nota
        Nota_string = min(self.samples_diccionario, key = lambda v: abs(self.samples_diccionario[v] - note.freq))
        Nota_MIDI_code = self.conv2midi(note.freq)
        Nota_MIDI_code_cercana = self.conv2midi(self.samples_diccionario[Nota_string])
        print(Nota_MIDI_code_cercana, Nota_MIDI_code)
        shift = Nota_MIDI_code - round(Nota_MIDI_code_cercana)
        print(shift)
        data , samplerate = soundfile.read(self.samples_directorio           + Nota_string)
                                         #"../Samples/" + instrumento + "/"  + " C4.wav "
        note_length = int(round(note.fs * note.duration))

        # Ahora pitcheamos la muestra para crear la nota que deseamos
        if int(shift) != 0:
            if note.duration == 0.0:
                note.note_signal = []
            else:
                time = len(data)/note_length
                #note_scaling
                nota_pitcheada = self.escalo_nota(data,samplerate,shift,time)
                volume_norm = 1
                if len(nota_pitcheada) > 0 and np.max(nota_pitcheada) is not 0:
                    volume_norm = 1.0 / np.amax(nota_pitcheada)

                note.note_signal = nota_pitcheada * note.velocity / 127 / 2  * volume_norm

        else:
            if note.duration == 0.0:
                note.note_signal = []
            else:
                scaling_factor = len(data)/note_length
                time_stretched_note = self.stretch(data, scaling_factor)
                volume_normalize = 1
                if len(time_stretched_note) > 0 and np.max(time_stretched_note) is not 0:
                    volume_normalize = 1.0 / np.amax(time_stretched_note)
                note.output_signal = time_stretched_note * note.velocity / 127 / 2 * volume_normalize

    #note scaling
    def escalo_nota(self, input_data, shift, time , DFT_size = 2**11 , hop_size = 2048//4):
        factor = 2**(1.0 * -1 *shift /12.0)
        DFT_size = 2**11
        stretched = self.stretch(input_data, len(input_data) / (len(input_data) * factor + DFT_size) * time )

        # cambio la velocidad

        input_data = stretched[DFT_size:]
        indices = np.round(np.arange(0, len(input_data), factor))  # Create an even-spaced array (input_data) spaced by the factor.
        indices = indices[indices < len(input_data)].astype(int)  # Astype int takes the neghboring values to these, but then preserves the same vector length.

        transposed = input_data[indices.astype(int)]
        return transposed.astype(input_data.dtype)



    def stretch(self, Y , factor , nfft=2048):
        #strecheo a Y por un factor
        stft = librosa.core.stft(Y, n_fft=nfft).transpose()
        stft_rows = stft.shape[0]
        stft_cols = stft.shape[1]

        times = np.arange(0, stft.shape[0], factor)  # times at which new FFT to be calculated
        hop = nfft / 4  # frame shift
        stft_new = np.zeros((len(times), stft_cols), dtype=np.complex_)
        phase_adv = (2 * np.pi * hop * np.arange(0, stft_cols)) / nfft
        phase = np.angle(stft[0])

        stft = np.concatenate((stft, np.zeros((1, stft_cols))), axis=0)

        for i, time in enumerate(times):
            left_frame = int(np.floor(time))
            local_frames = stft[[left_frame, left_frame + 1], :]
            right_wt = time - np.floor(time)
            local_mag = (1 - right_wt) * np.absolute(local_frames[0, :]) + right_wt * np.absolute(local_frames[1, :])
            local_dphi = np.angle(local_frames[1, :]) - np.angle(local_frames[0, :]) - phase_adv
            local_dphi = local_dphi - 2 * np.pi * np.floor(local_dphi / (2 * np.pi))
            stft_new[i, :] = local_mag * np.exp(phase * 1j)
            phase += local_dphi + phase_adv

        return librosa.core.istft(stft_new.transpose())


    def conv2midi(self,frecuencia):
        return 12 * np.log2(frecuencia * 32 / 440) + 9


    def proceso_samples(self, instrumento):
        #Creo un diccionario de la forma: [nota , frecuencia]
        self.samples_directorio = "../Samples/" + instrumento + "/"

        for sample in os.listdir(self.samples_directorio):
            nota_file = sample.split(".")
            print(nota_file[0])

            self.samples_diccionario[sample] = self.Notas_que_hay_en_sample[nota_file[0]]
            # ej forma de diccionario:
            # {'C3.wav': 130.813,
            #  'C4.wav': 261.626,
            #  'C5.wav': 523.251}

    def creo_my_diccionario(self):
        self.Notas_que_hay_en_sample = {}
        NOTAS = ["A0", "Bb0", "B0",
                       "C1", "Db1", "D1", "Eb1", "E1", "F1", "Gb1", "G1", "Ab1", "A1", "Bb1", "B1",
                       "C2", "Db2", "D2", "Eb2", "E2", "F2", "Gb2", "G2", "Ab2", "A2", "Bb2", "B2",
                       "C3", "Db3", "D3", "Eb3", "E3", "F3", "Gb3", "G3", "Ab3", "A3", "Bb3", "B3",
                       "C4", "Db4", "D4", "Eb4", "E4", "F4", "Gb4", "G4", "Ab4", "A4", "Bb4", "B4",
                       "C5", "Db5", "D5", "Eb5", "E5", "F5", "Gb5", "G5", "Ab5", "A5", "Bb5", "B5",
                       "C6", "Db6", "D6", "Eb6", "E6", "F6", "Gb6", "G6", "Ab6", "A6", "Bb6", "B6",
                       "C7", "Db7", "D7", "Eb7", "E7", "F7", "Gb7", "G7", "Ab7", "A7", "Bb7", "B7",
                       "C8"]
        i = 0
        for note in NOTAS:
            prev_freq = round(440 / 32 * (2 ** (((21 + i) - 9) / 12)), 3)
            self.Notas_que_hay_en_sample[note] = prev_freq
            i += 1