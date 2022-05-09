from Frontend.scr.menu import MenuWindow
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':


    app = QApplication([])
    window = MenuWindow()
    window.show()

    app.exec()