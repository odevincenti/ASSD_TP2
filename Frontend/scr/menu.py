import numpy as np
from PyQt5.QtWidgets import QWidget
from Frontend.scr.ui.menu import Ui_Form

class MenuWindow (QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.label_track0.hide()
        self.pushButton_instrument_track0.hide()
        self.horizontalSlider_track0.hide()
        self.pushButton_mute_track0.hide()

        self.pushButton_Upload.clicked.connect(self.get_mid_file)
        self.pushButton_Save.clicked.connect(self.save_file)
        self.pushButton_Sintetizar.clicked.connect(self.sintetizar_exe)
        self.pushButton_graficar.clicked.connect(self.graficar_espectrograma)

        self.pushButton_play.clicked.connect(self.play_song)
        self.pushButton_pausa.clicked.connect(self.pause_song)
        self.pushButton_rec.clicked.connect(self.reset_song)





    def get_mid_file(self):
        print("upload")

    def save_file(self):
        print("save")

    def sintetizar_exe(self):
        print("sintetizar")

    def graficar_espectrograma(self):
        print("graficar espectrograma")


    def play_song(self):
        print("pone play maestro")


    def pause_song(self):
        print("para la motoneta rey")


    def reset_song(self):
        print("ponela de vuelta que es un temazo")