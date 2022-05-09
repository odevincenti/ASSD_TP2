from PyQt5.QtWidgets import QWidget
from Frontend.scr.ui.track import Ui_Form

class TrackWidget (QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.setupUi(self)
