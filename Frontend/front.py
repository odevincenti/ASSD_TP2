from Frontend.scr.menu import MenuWindow
from PyQt5.QtWidgets import QApplication
import scr.ui.nota
import scr.ui.play
import scr.ui.pause
import scr.ui.stop

if __name__ == '__main__':

    app = QApplication([])
    window = MenuWindow()
    window.show()

    app.exec()