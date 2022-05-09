import numpy as np
import sys
from Frontend.scr.track import TrackWidget
from src.backend import *
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from Frontend.scr.ui.menu import Ui_Form

class MenuWindow (QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.back = backend()
        self.track_array = []

        notes = QPixmap("notes50x50.png")
        self.label_3.setPixmap(notes)

        self.label_track0.hide()
        self.pushButton_instrument_track0.hide()
        self.horizontalSlider_track0.hide()
        self.pushButton_mute_track0.hide()

        self.pushButton_Upload.clicked.connect(self.get_mid_file)
        self.pushButton_Save.clicked.connect(self.save_file)
        self.pushButton_Sintetizar.clicked.connect(self.sintetizar)
        self.pushButton_graficar.clicked.connect(self.graficar_espectrograma)

        self.pushButton_play.clicked.connect(self.play_song)
        self.pushButton_pausa.clicked.connect(self.pause_song)
        self.pushButton_rec.clicked.connect(self.reset_song)





    def get_mid_file(self):
        print("upload")
        filename = QFileDialog.getOpenFileNames()
        self.path = filename[0][0]
        print(self.path)
        self.back.update_path(self.path)
        self.ammount_of_tracks = self.back.quantity_of_tracks()
        print("cantidad de tracks:")
        print(self.ammount_of_tracks)

        for i in range(1, self.ammount_of_tracks + 1):
            self.aux_track = TrackWidget()
            self.aux_track.label_track.setText("Track " + str(i))
            self.track_array.append(self.aux_track)
            self.Track_Widget.layout().addWidget(self.aux_track)


    def save_file(self):
        print("save")
        self.back.save_wav_file(self.path)

    def sintetizar(self):
        print("sintetizar")
        self.back.synthesize_song()

    def graficar_espectrograma(self):
        print("graficar espectrograma")


    def play_song(self):
        print("pone play maestro")
        self.back.play_song()


    def pause_song(self):
        print("para la motoneta rey")
        self.back.pause_reproduction()


    def reset_song(self):
        print("ponela de vuelta que es un temazo")