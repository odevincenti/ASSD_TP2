from PyQt5.QtWidgets import QWidget
from Frontend.scr.ui.track import Ui_Form

class TrackWidget (QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.setupUi(self)
        self.mute = 0

        self.pushButton_mute_track.clicked.connect(self.mute_track)

    def instrument_track(self):
        print("instrumento para oir")

    def mute_track(self):
        if self.mute == 0:
            self.pushButton_mute_track.setStyleSheet("background: red")
            self.mute = 1
        else:
            self.pushButton_mute_track.setStyleSheet("background: green")
            self.mute = 0