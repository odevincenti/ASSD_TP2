from PyQt5.QtWidgets import QWidget
from Frontend.scr.ui.track import Ui_Form

class TrackWidget (QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.setupUi(self)
        self.mute = True
        self.velocity = 0
        self.instrument = ''

        self.pushButton_mute_track.clicked.connect(self.mute_track)

    def instrument_track(self):
        if self.comboBox_track.currentIndex() == 0:
            self.instrument = 'P'
        elif self.comboBox_track.currentIndex() == 1:
            self.instrument = 'F'
        elif self.comboBox_track.currentIndex() == 2:
            self.instrument = 'G'
        else:
            self.instrument = 'T'

    def mute_track(self):
        if self.mute == True:
            self.pushButton_mute_track.setStyleSheet("background: red;\n"
                                    "color: black;")
            self.mute = False
        else:
            self.pushButton_mute_track.setStyleSheet("background: green;\n"
                                                     "color: white;")
            self.mute = True

    def get_velocity(self):
        self.velocity = self.horizontalSlider_track.value()