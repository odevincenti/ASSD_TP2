from Frontend.scr.track import TrackWidget
from Frontend.counter import Counter
from src.backend import *
from PyQt5.QtWidgets import *
from Frontend.scr.ui.menu import Ui_Menu
from pathlib import Path


class MenuWindow (QWidget, Ui_Menu):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.back = backend()
        self.track_array = []
        self.first_time = 0

        #TRACK 0
        self.label_track0.hide()
        self.comboBox_track0.hide()
        self.horizontalSlider_track0.hide()
        self.pushButton_mute_track0.hide()


        #BUTTONS
        self.pushButton_Upload.clicked.connect(self.get_mid_file)
        self.pushButton_Save.clicked.connect(self.save_file)
        self.pushButton_Sintetizar.clicked.connect(self.sintetizar)
        self.pushButton_graficar.clicked.connect(self.graficar_espectrograma)

        self.pushButton_play.clicked.connect(self.play_song)
        self.pushButton_pausa.clicked.connect(self.pause_song)
        self.pushButton_rec.clicked.connect(self.reset_song)

        #MPLWIDGET
        self.MplWidget.show_toolbar(self.ToolBar)

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

        self.horizontalSlider_Track.setMaximum(self.back.song.duration)
        print(self.horizontalSlider_Track.value())

    def save_file(self):
        print("save")
        self.back.save_wav_file(self.path_name)

    def sintetizar(self):
        print("sintetizar")
        self.back.process_song()


    def graficar_espectrograma(self):
        print("graficar espectrograma")
        self.MplWidget.canvas.ax.clear()
        self.MplWidget.graph_spectro(self.MplWidget.canvas.ax, self.MplWidget.figure)
        self.MplWidget.canvas.draw()

    def play_song(self):
        print("PLAY")
        if self.first_time == 0:
            self.counter.start_thread()
            self.first_time = 1
        self.counter.pause_loop = False
        self.back.play_song()


    def pause_song(self):
        print("PAUSA")
        self.counter.pause_loop = True
        self.back.pause_reproduction()


    def reset_song(self):
        print("RESET")
        self.counter.reset_loop = True
        self.counter.start()



    def Reverb_check_state(self, value):
        print("REVERB BOX")
        #if value != 0:
            #self.verticalSlider_Reverb_Retraso.value()
            #self.verticalSlider_Reverb_Ganancia.value()


    def Echo_check_state(self, value):
        print("ECHO BOX")
        # if value != 0:
            #self.verticalSlider_Echo_Retraso.value()
            #self.verticalSlider_Echo_Ganancia.value()


    def Flanger_check_state(self, value):
        print("FLANGER BOX")
        # if value != 0:
            #self.verticalSlider_Flanger_Retraso.value()
            #self.verticalSlider_flanger_frecuencia_2.value()
            #self.verticalSlider_Flanger_Ganancia.value()