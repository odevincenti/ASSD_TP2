from PyQt5.QtWidgets import QWidget
from Frontend.scr.ui.track import Ui_Form

class TrackWidget (QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.setupUi(self)
        self.color = 0

        self.pushButton_instrument_track.clicked.connect(self.instrument_track)
        self.pushButton_mute_track.clicked.connect(self.mute_track)

    def instrument_track(self):
        print("instrumento para oir")

    def mute_track(self):
        if self.color == 0:
            self.pushButton_mute_track.setStyleSheet("background: red")
            self.color = 1
        else:
            self.pushButton_mute_track.setStyleSheet("background: green")
            self.color = 0