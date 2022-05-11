from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt


#se crea una widget con 1 layout
#adentro hay un canvas con una figura

class MplWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.canvas)  #agrego el canvas

        self.canvas.ax = self.canvas.figure.add_subplot(111)
        self.setLayout(self.layout)
        #self.canvas.draw()

    def show_toolbar(self, layout):
        #self.toolbar.setStyleSheet("background-color:Gray;")
        layout.addWidget(NavigationToolbar(self.canvas, self))
        self.canvas.toolbar.setStyleSheet("backgroud-color:Red;")

    def graph_spectro(self, ax, figure):

        dt = 0.001
        t = np.arange(0, 2, dt)
        f0 = 50
        f1 = 250
        t1 = 2
        x = np.cos(2 * np.pi * t * (f0 + (f1 - f0) * np.power(t, 2) / (3 * t1 ** 2)))

        fs = 1/dt
        sd.play(2 * x, fs)

        #im = ax.imshow(np.arange(100, 0, -1).reshape(10, 10))
        #figure.colorbar(im)

        ax.specgram(x, NFFT=128, Fs=1/dt, noverlap=120, cmap='jet_r')





