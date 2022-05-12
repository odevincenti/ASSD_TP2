from scr.track import TrackWidget
from counter import Counter
from src.backend import *
from PyQt5.QtWidgets import *
from scr.ui.menu import Ui_Menu
from pathlib import Path


class MenuWindow (QWidget, Ui_Menu):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.back = backend()
        self.track_array = []
        self.first_time = 0
        self.pausa = False
        self.play = True
        self.pause = True

        #TRACK 0
        self.label_track0.hide()
        self.comboBox_track0.hide()
        self.horizontalSlider_track0.hide()
        self.pushButton_mute_track0.hide()


        #BUTTONS
        self.pushButton_Upload.clicked.connect(self.get_mid_file)
        self.pushButton_Save.clicked.connect(self.save_file)
        self.pushButton_Sintetizar.clicked.connect(self.sintetizar)

        self.pushButton_play.clicked.connect(self.play_song)
        self.pushButton_pausa.clicked.connect(self.pause_song)
        self.pushButton_rec.clicked.connect(self.reset_song)


        #CHECKBOXES
        self.checkBox_Reverb.stateChanged.connect(self.Reverb_check_state)
        self.checkBox_Echo.stateChanged.connect(self.Echo_check_state)
        self.checkBox_Flanger.stateChanged.connect(self.Flanger_check_state)



    def get_mid_file(self):
        print("upload")
        filename = QFileDialog.getOpenFileNames()
        self.path = filename[0][0]
        self.path_name = Path(self.path)

        self.back.update_path(self.path_name)
        self.ammount_of_tracks = self.back.quantity_of_tracks()
        print("cantidad de tracks:")
        print(self.ammount_of_tracks)

        for i in range(1, self.ammount_of_tracks + 1):
            self.aux_track = TrackWidget()
            self.aux_track.label_track.setText("Track " + str(i))
            self.track_array.append(self.aux_track)
            self.Track_Widget.layout().addWidget(self.aux_track)

        self.counter = Counter(self, self.back.song.duration)

        self.horizontalSlider_Track.setMaximum(int(self.back.song.duration))
        print(self.horizontalSlider_Track.value())

    def save_file(self):
        print("save")
        wav_path = Path(self.path)
        wav_path = Path(str(wav_path.parent) + '/' + str(wav_path.stem) + '.wav')
        print(wav_path)
        self.back.save_wav_file(wav_path)

    def sintetizar(self):
        print("sintetizar")
        self.counter.reset_loop = True
        for i in range(1, self.ammount_of_tracks + 1):
            self.back.update_track(i-1, self.track_array[i-1].get_instrument(), self.track_array[i-1].mute, self.track_array[i-1].get_velocity())
        self.counter.reset()
        self.back.process_song()


    def play_song(self):
        print("PLAY")
        if self.first_time == 0:
            self.pausa = False
            self.counter.start_thread()
            self.first_time = 1
        if self.pausa == False:
            self.counter.pause_loop = False
            self.back.play_song()
        else:
            if(self.play):
                self.pause = True
                self.counter.pause_loop = False
                self.back.resume_song(self.counter.play_seconds)
                self.play = False


    def pause_song(self):
        print("PAUSA")
        if(self.pause):
            self.pausa = True
            self.play = True
            self.pause = False
            self.counter.pause_loop = True
            self.back.pause_reproduction()


    def reset_song(self):
        print("RESET")
        self.play = False
        self.pausa = False
        self.pause = True
        self.counter.reset_loop = True
        self.counter.start()
        self.back.pause_reproduction()
        self.back.play_song()


    def Reverb_check_state(self, value):
        print("REVERB BOX")
        if value != 0:
            self.back.all_pass_effect(self.verticalSlider_Reverb_Ganancia.value(), self.verticalSlider_Reverb_Retraso.value())


    def Echo_check_state(self, value):
        print("ECHO BOX")
        if value != 0:
            self.back.echo_effect(self.verticalSlider_Echo_Ganancia.value(), self.verticalSlider_Echo_Retraso.value())


    def Flanger_check_state(self, value):
        print("FLANGER BOX")
        if value != 0:
            self.back.flanger_effect(self.verticalSlider_Flanger_Ganancia.value(), self.verticalSlider_Flanger_Retraso.value(), self.verticalSlider_flanger_frecuencia_2.value())
