# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(1305, 738)
        Menu.setStyleSheet("background:rgb(30,30,30);\n"
"color:white;\n"
"")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(Menu)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Menu)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("background:rgb(30,30,30);\n"
"color:black;\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("background:rgb(30,30,30);\n"
"color:white;")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_Upload = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Upload.setFont(font)
        self.pushButton_Upload.setStyleSheet("background:white;\n"
"color:black;")
        self.pushButton_Upload.setObjectName("pushButton_Upload")
        self.horizontalLayout_3.addWidget(self.pushButton_Upload)
        self.pushButton_Save = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Save.setFont(font)
        self.pushButton_Save.setStyleSheet("background:white;\n"
"color:black;")
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.horizontalLayout_3.addWidget(self.pushButton_Save)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_9.addItem(spacerItem)
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMaximumSize(QtCore.QSize(555, 515))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 422, 513))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.Track_Widget = QtWidgets.QWidget(self.scrollAreaWidgetContents_3)
        self.Track_Widget.setMaximumSize(QtCore.QSize(400, 16777215))
        self.Track_Widget.setStyleSheet("background:rgb(30,30,30);")
        self.Track_Widget.setObjectName("Track_Widget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.Track_Widget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widget = QtWidgets.QWidget(self.Track_Widget)
        self.widget.setMaximumSize(QtCore.QSize(400, 100))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.track0 = QtWidgets.QHBoxLayout()
        self.track0.setObjectName("track0")
        self.label_track0 = QtWidgets.QLabel(self.widget)
        self.label_track0.setStyleSheet("color:white;")
        self.label_track0.setObjectName("label_track0")
        self.track0.addWidget(self.label_track0)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.track0.addItem(spacerItem1)
        self.comboBox_track0 = QtWidgets.QComboBox(self.widget)
        self.comboBox_track0.setStyleSheet("background:white;\n"
"color:black;")
        self.comboBox_track0.setObjectName("comboBox_track0")
        self.comboBox_track0.addItem("")
        self.comboBox_track0.addItem("")
        self.comboBox_track0.addItem("")
        self.comboBox_track0.addItem("")
        self.track0.addWidget(self.comboBox_track0)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.track0.addItem(spacerItem2)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_10.addItem(spacerItem3)
        self.horizontalSlider_track0 = QtWidgets.QSlider(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(22)
        sizePolicy.setHeightForWidth(self.horizontalSlider_track0.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_track0.setSizePolicy(sizePolicy)
        self.horizontalSlider_track0.setMaximumSize(QtCore.QSize(80, 22))
        self.horizontalSlider_track0.setStyleSheet("QSlider::groove:horizontal{\n"
"    border: 1px solid black;\n"
"    height: 3px;\n"
"    width: 50px;\n"
"    background: cyan;\n"
"}\n"
"\n"
"QSlider::handle:horizontal{\n"
"    background: cyan;\n"
"    border: 1px solid black;\n"
"    width: 6px;\n"
"    margin: -8px 0;\n"
"    boder-radius: 9px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal{\n"
"    background-color: white;\n"
"}")
        self.horizontalSlider_track0.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_track0.setObjectName("horizontalSlider_track0")
        self.verticalLayout_10.addWidget(self.horizontalSlider_track0)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_10.addItem(spacerItem4)
        self.track0.addLayout(self.verticalLayout_10)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.track0.addItem(spacerItem5)
        self.pushButton_mute_track0 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_mute_track0.setFont(font)
        self.pushButton_mute_track0.setStyleSheet("background:green;\n"
"color:white;")
        self.pushButton_mute_track0.setObjectName("pushButton_mute_track0")
        self.track0.addWidget(self.pushButton_mute_track0)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.track0.addItem(spacerItem6)
        self.verticalLayout_3.addLayout(self.track0)
        self.verticalLayout_9.addWidget(self.widget)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_9.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem8)
        self.verticalLayout_8.addLayout(self.verticalLayout_9)
        self.verticalLayout_11.addWidget(self.Track_Widget)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_11.addItem(spacerItem9)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_9.addWidget(self.scrollArea)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.pushButton_Sintetizar = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Sintetizar.setFont(font)
        self.pushButton_Sintetizar.setStyleSheet("background:green;\n"
"color:white;")
        self.pushButton_Sintetizar.setObjectName("pushButton_Sintetizar")
        self.verticalLayout_2.addWidget(self.pushButton_Sintetizar)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSlider_Track = QtWidgets.QSlider(self.tab)
        self.horizontalSlider_Track.setStyleSheet("QSlider::groove:horizontal{\n"
"    border: 1px solid black;\n"
"    height: 5px;\n"
"    background: white;\n"
"}\n"
"\n"
"QSlider::handle:horizontal{\n"
"    background: white;\n"
"    border: 1px solid black;\n"
"    width: 8px;\n"
"    margin: -3px 0;\n"
"    boder-radius: 9px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal{\n"
"    background-color: black;\n"
"}")
        self.horizontalSlider_Track.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_Track.setObjectName("horizontalSlider_Track")
        self.horizontalLayout.addWidget(self.horizontalSlider_Track)
        self.label_3 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(50, 50))
        self.label_3.setStyleSheet("image: url(:/notes50x50/notes50x50.png);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/nota/notes50x50.png"))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout_16.addLayout(self.horizontalLayout)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem10)
        self.pushButton_play = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.pushButton_play.sizePolicy().hasHeightForWidth())
        self.pushButton_play.setSizePolicy(sizePolicy)
        self.pushButton_play.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_play.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_play.setFont(font)
        self.pushButton_play.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_play.setStyleSheet("QPushButton{\n"
"    border-image: url(:/play/play.png);\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: black;\n"
"}")
        self.pushButton_play.setText("")
        self.pushButton_play.setObjectName("pushButton_play")
        self.horizontalLayout_15.addWidget(self.pushButton_play)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_15.addItem(spacerItem11)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem12)
        self.pushButton_pausa = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.pushButton_pausa.sizePolicy().hasHeightForWidth())
        self.pushButton_pausa.setSizePolicy(sizePolicy)
        self.pushButton_pausa.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_pausa.setFont(font)
        self.pushButton_pausa.setStyleSheet("QPushButton{\n"
"    border-image: url(:/pause/pause.png);\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: black;\n"
"}")
        self.pushButton_pausa.setText("")
        self.pushButton_pausa.setObjectName("pushButton_pausa")
        self.horizontalLayout_15.addWidget(self.pushButton_pausa)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem13)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_15.addItem(spacerItem14)
        self.pushButton_rec = QtWidgets.QPushButton(self.tab)
        self.pushButton_rec.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_rec.setFont(font)
        self.pushButton_rec.setStyleSheet("QPushButton{\n"
"    border-image: url(:/stop/stop.png);\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: black;\n"
"}")
        self.pushButton_rec.setText("")
        self.pushButton_rec.setObjectName("pushButton_rec")
        self.horizontalLayout_15.addWidget(self.pushButton_rec)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem15)
        self.verticalLayout_16.addLayout(self.horizontalLayout_15)
        self.verticalLayout_15.addLayout(self.verticalLayout_16)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.line_3 = QtWidgets.QFrame(self.tab)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line_3.setFont(font)
        self.line_3.setAutoFillBackground(False)
        self.line_3.setStyleSheet("border: 5px solid white;\n"
"border-style: inset;")
        self.line_3.setLineWidth(1)
        self.line_3.setMidLineWidth(5)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_17.addWidget(self.line_3)
        self.verticalLayout_15.addLayout(self.verticalLayout_17)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout()
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.checkBox_Reverb = QtWidgets.QCheckBox(self.tab)
        self.checkBox_Reverb.setStyleSheet("color:white;")
        self.checkBox_Reverb.setObjectName("checkBox_Reverb")
        self.verticalLayout_30.addWidget(self.checkBox_Reverb)
        self.horizontalLayout_26.addLayout(self.verticalLayout_30)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem16)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout()
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.lcdNumber_Reverb_Retraso = QtWidgets.QLCDNumber(self.tab)
        self.lcdNumber_Reverb_Retraso.setStyleSheet("color:white;")
        self.lcdNumber_Reverb_Retraso.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_Reverb_Retraso.setObjectName("lcdNumber_Reverb_Retraso")
        self.verticalLayout_31.addWidget(self.lcdNumber_Reverb_Retraso)
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setStyleSheet("color:white;")
        self.label_15.setObjectName("label_15")
        self.verticalLayout_31.addWidget(self.label_15)
        self.horizontalLayout_27.addLayout(self.verticalLayout_31)
        self.verticalSlider_Reverb_Retraso = QtWidgets.QSlider(self.tab)
        self.verticalSlider_Reverb_Retraso.setStyleSheet("QSlider::groove:vertical{\n"
"    border: 1px solid black;\n"
"    height: 110px;\n"
"    width: 5px;\n"
"    background: white;\n"
"}\n"
"\n"
"QSlider::handle:vertical{\n"
"    background: cyan;\n"
"    border: 1px solid black;\n"
"    width: 10px;\n"
"    margin: -5px -10px;\n"
"    boder-radius: 9px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical{\n"
"    background-color: cyan;\n"
"    border: 1px solid black;\n"
"}")
        self.verticalSlider_Reverb_Retraso.setMaximum(30)
        self.verticalSlider_Reverb_Retraso.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_Reverb_Retraso.setObjectName("verticalSlider_Reverb_Retraso")
        self.horizontalLayout_27.addWidget(self.verticalSlider_Reverb_Retraso)
        self.horizontalLayout_26.addLayout(self.horizontalLayout_27)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem17)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout()
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.lcdNumber_Reverb_Ganancia = QtWidgets.QLCDNumber(self.tab)
        self.lcdNumber_Reverb_Ganancia.setStyleSheet("color:white;")
        self.lcdNumber_Reverb_Ganancia.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_Reverb_Ganancia.setObjectName("lcdNumber_Reverb_Ganancia")
        self.verticalLayout_32.addWidget(self.lcdNumber_Reverb_Ganancia)
        self.label_16 = QtWidgets.QLabel(self.tab)
        self.label_16.setStyleSheet("color:white;")
        self.label_16.setObjectName("label_16")
        self.verticalLayout_32.addWidget(self.label_16)
        self.horizontalLayout_28.addLayout(self.verticalLayout_32)
        self.verticalSlider_Reverb_Ganancia = QtWidgets.QSlider(self.tab)
        self.verticalSlider_Reverb_Ganancia.setStyleSheet("QSlider::groove:vertical{\n"
"    border: 1px solid black;\n"
"    height: 110px;\n"
"    width: 5px;\n"
"    background: white;\n"
"}\n"
"\n"
"QSlider::handle:vertical{\n"
"    background: cyan;\n"
"    border: 1px solid black;\n"
"    width: 10px;\n"
"    margin: -5px -10px;\n"
"    boder-radius: 9px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical{\n"
"    background-color: cyan;\n"
"    border: 1px solid black;\n"
"}")
        self.verticalSlider_Reverb_Ganancia.setMaximum(100)
        self.verticalSlider_Reverb_Ganancia.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_Reverb_Ganancia.setObjectName("verticalSlider_Reverb_Ganancia")
        self.horizontalLayout_28.addWidget(self.verticalSlider_Reverb_Ganancia)
        self.horizontalLayout_26.addLayout(self.horizontalLayout_28)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem18)
        self.verticalLayout_15.addLayout(self.horizontalLayout_26)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.line_2 = QtWidgets.QFrame(self.tab)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line_2.setFont(font)
        self.line_2.setAutoFillBackground(False)
        self.line_2.setStyleSheet("border: 5px solid white;\n"
"border-style: inset;")
        self.line_2.setLineWidth(1)
        self.line_2.setMidLineWidth(5)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_20.addWidget(self.line_2)
        self.verticalLayout_15.addLayout(self.verticalLayout_20)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout()
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.checkBox_Echo = QtWidgets.QCheckBox(self.tab)
        self.checkBox_Echo.setStyleSheet("color:white;")
        self.checkBox_Echo.setObjectName("checkBox_Echo")
        self.verticalLayout_27.addWidget(self.checkBox_Echo)
        self.horizontalLayout_19.addLayout(self.verticalLayout_27)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem19)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.lcdNumber_Echo_Retraso = QtWidgets.QLCDNumber(self.tab)
        self.lcdNumber_Echo_Retraso.setStyleSheet("color:white;")
        self.lcdNumber_Echo_Retraso.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_Echo_Retraso.setObjectName("lcdNumber_Echo_Retraso")
        self.verticalLayout_21.addWidget(self.lcdNumber_Echo_Retraso)
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setStyleSheet("color:white;")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_21.addWidget(self.label_10)
        self.horizontalLayout_20.addLayout(self.verticalLayout_21)
        self.verticalSlider_Echo_Retraso = QtWidgets.QSlider(self.tab)
        self.verticalSlider_Echo_Retraso.setStyleSheet("QSlider::groove:vertical{\n"
"    border: 1px solid black;\n"
"    height: 110px;\n"
"    width: 5px;\n"
"    background: white;\n"
"}\n"
"\n"
"QSlider::handle:vertical{\n"
"    background: cyan;\n"
"    border: 1px solid black;\n"
"    width: 10px;\n"
"    margin: -5px -10px;\n"
"    boder-radius: 9px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical{\n"
"    background-color: cyan;\n"
"    border: 1px solid black;\n"
"}")
        self.verticalSlider_Echo_Retraso.setMaximum(500)
        self.verticalSlider_Echo_Retraso.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_Echo_Retraso.setObjectName("verticalSlider_Echo_Retraso")
        self.horizontalLayout_20.addWidget(self.verticalSlider_Echo_Retraso)
        self.horizontalLayout_19.addLayout(self.horizontalLayout_20)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem20)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.lcdNumber_Echo_Ganancia = QtWidgets.QLCDNumber(self.tab)
        self.lcdNumber_Echo_Ganancia.setStyleSheet("color:white;")
        self.lcdNumber_Echo_Ganancia.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_Echo_Ganancia.setObjectName("lcdNumber_Echo_Ganancia")
        self.verticalLayout_22.addWidget(self.lcdNumber_Echo_Ganancia)
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setStyleSheet("color:white;")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_22.addWidget(self.label_11)
        self.horizontalLayout_21.addLayout(self.verticalLayout_22)
        self.verticalSlider_Echo_Ganancia = QtWidgets.QSlider(self.tab)
        self.verticalSlider_Echo_Ganancia.setStyleSheet("QSlider::groove:vertical{\n"
"    border: 1px solid black;\n"
"    height: 110px;\n"
"    width: 5px;\n"
"    background: white;\n"
"}\n"
"\n"
"QSlider::handle:vertical{\n"
"    background: cyan;\n"
"    border: 1px solid black;\n"
"    width: 10px;\n"
"    margin: -5px -10px;\n"
"    boder-radius: 9px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical{\n"
"    background-color: cyan;\n"
"    border: 1px solid black;\n"
"}")
        self.verticalSlider_Echo_Ganancia.setMaximum(100)
        self.verticalSlider_Echo_Ganancia.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_Echo_Ganancia.setObjectName("verticalSlider_Echo_Ganancia")
        self.horizontalLayout_21.addWidget(self.verticalSlider_Echo_Ganancia)
        self.horizontalLayout_19.addLayout(self.horizontalLayout_21)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem21)
        self.verticalLayout_15.addLayout(self.horizontalLayout_19)
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.line = QtWidgets.QFrame(self.tab)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line.setFont(font)
        self.line.setAutoFillBackground(False)
        self.line.setStyleSheet("border: 5px solid white;\n"
"border-style: inset;")
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_23.addWidget(self.line)
        self.verticalLayout_15.addLayout(self.verticalLayout_23)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout()
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.checkBox_Flanger = QtWidgets.QCheckBox(self.tab)
        self.checkBox_Flanger.setStyleSheet("color:white;")
        self.checkBox_Flanger.setObjectName("checkBox_Flanger")
        self.verticalLayout_29.addWidget(self.checkBox_Flanger)
        self.horizontalLayout_22.addLayout(self.verticalLayout_29)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem22)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.lcdNumber_Flanger_Retraso = QtWidgets.QLCDNumber(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_Flanger_Retraso.sizePolicy().hasHeightForWidth())
        self.lcdNumber_Flanger_Retraso.setSizePolicy(sizePolicy)
        self.lcdNumber_Flanger_Retraso.setStyleSheet("color:white;")
        self.lcdNumber_Flanger_Retraso.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_Flanger_Retraso.setObjectName("lcdNumber_Flanger_Retraso")
        self.verticalLayout_24.addWidget(self.lcdNumber_Flanger_Retraso)
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setStyleSheet("color:white;")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_24.addWidget(self.label_12)
        self.horizontalLayout_23.addLayout(self.verticalLayout_24)
        self.verticalSlider_Flanger_Retraso = QtWidgets.QSlider(self.tab)
        self.verticalSlider_Flanger_Retraso.setStyleSheet("QSlider::groove:vertical{\n"
"    border: 1px solid black;\n"
"    height: 110px;\n"
"    width: 5px;\n"
"    background: white;\n"
"}\n"
"\n"
"QSlider::handle:vertical{\n"
"    background: cyan;\n"
"    border: 1px solid black;\n"
"    width: 10px;\n"
"    margin: -5px -10px;\n"
"    boder-radius: 9px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical{\n"
"    background-color: cyan;\n"
"    border: 1px solid black;\n"
"}")
        self.verticalSlider_Flanger_Retraso.setMaximum(500)
        self.verticalSlider_Flanger_Retraso.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_Flanger_Retraso.setObjectName("verticalSlider_Flanger_Retraso")
        self.horizontalLayout_23.addWidget(self.verticalSlider_Flanger_Retraso)
        self.horizontalLayout_22.addLayout(self.horizontalLayout_23)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem23)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.lcdNumber_Flanger_Frecuencia = QtWidgets.QLCDNumber(self.tab)
        self.lcdNumber_Flanger_Frecuencia.setStyleSheet("color:white;")
        self.lcdNumber_Flanger_Frecuencia.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_Flanger_Frecuencia.setObjectName("lcdNumber_Flanger_Frecuencia")
        self.verticalLayout_25.addWidget(self.lcdNumber_Flanger_Frecuencia)
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setStyleSheet("color:white;")
        self.label_13.setObjectName("label_13")
        self.verticalLayout_25.addWidget(self.label_13)
        self.horizontalLayout_24.addLayout(self.verticalLayout_25)
        self.verticalSlider_flanger_frecuencia_2 = QtWidgets.QSlider(self.tab)
        self.verticalSlider_flanger_frecuencia_2.setStyleSheet("QSlider::groove:vertical{\n"
"    border: 1px solid black;\n"
"    height: 110px;\n"
"    width: 5px;\n"
"    background: white;\n"
"}\n"
"\n"
"QSlider::handle:vertical{\n"
"    background: cyan;\n"
"    border: 1px solid black;\n"
"    width: 10px;\n"
"    margin: -5px -10px;\n"
"    boder-radius: 9px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical{\n"
"    background-color: cyan;\n"
"    border: 1px solid black;\n"
"}")
        self.verticalSlider_flanger_frecuencia_2.setMaximum(10000)
        self.verticalSlider_flanger_frecuencia_2.setSingleStep(10)
        self.verticalSlider_flanger_frecuencia_2.setPageStep(1)
        self.verticalSlider_flanger_frecuencia_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_flanger_frecuencia_2.setObjectName("verticalSlider_flanger_frecuencia_2")
        self.horizontalLayout_24.addWidget(self.verticalSlider_flanger_frecuencia_2)
        self.horizontalLayout_22.addLayout(self.horizontalLayout_24)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem24)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout()
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.lcdNumber_Flanger_Ganancia = QtWidgets.QLCDNumber(self.tab)
        self.lcdNumber_Flanger_Ganancia.setStyleSheet("color:white;")
        self.lcdNumber_Flanger_Ganancia.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_Flanger_Ganancia.setObjectName("lcdNumber_Flanger_Ganancia")
        self.verticalLayout_26.addWidget(self.lcdNumber_Flanger_Ganancia)
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setStyleSheet("color:white;")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_26.addWidget(self.label_14)
        self.horizontalLayout_25.addLayout(self.verticalLayout_26)
        self.verticalSlider_Flanger_Ganancia = QtWidgets.QSlider(self.tab)
        self.verticalSlider_Flanger_Ganancia.setStyleSheet("QSlider::groove:vertical{\n"
"    border: 1px solid black;\n"
"    height: 110px;\n"
"    width: 5px;\n"
"    background: white;\n"
"}\n"
"\n"
"QSlider::handle:vertical{\n"
"    background: cyan;\n"
"    border: 1px solid black;\n"
"    width: 10px;\n"
"    margin: -5px -10px;\n"
"    boder-radius: 9px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical{\n"
"    background-color: cyan;\n"
"    border: 1px solid black;\n"
"}")
        self.verticalSlider_Flanger_Ganancia.setMaximum(100)
        self.verticalSlider_Flanger_Ganancia.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_Flanger_Ganancia.setObjectName("verticalSlider_Flanger_Ganancia")
        self.horizontalLayout_25.addWidget(self.verticalSlider_Flanger_Ganancia)
        self.horizontalLayout_22.addLayout(self.horizontalLayout_25)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem25)
        self.verticalLayout_15.addLayout(self.horizontalLayout_22)
        self.line_4 = QtWidgets.QFrame(self.tab)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line_4.setFont(font)
        self.line_4.setAutoFillBackground(False)
        self.line_4.setStyleSheet("border: 5px solid white;\n"
"border-style: inset;")
        self.line_4.setLineWidth(1)
        self.line_4.setMidLineWidth(5)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_15.addWidget(self.line_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_15)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.verticalLayout_7.addLayout(self.verticalLayout)

        self.retranslateUi(Menu)
        self.tabWidget.setCurrentIndex(0)
        self.verticalSlider_Flanger_Retraso.valueChanged['int'].connect(self.lcdNumber_Flanger_Retraso.display) # type: ignore
        self.verticalSlider_Reverb_Retraso.valueChanged['int'].connect(self.lcdNumber_Reverb_Retraso.display) # type: ignore
        self.verticalSlider_flanger_frecuencia_2.valueChanged['int'].connect(self.lcdNumber_Flanger_Frecuencia.display) # type: ignore
        self.verticalSlider_Reverb_Ganancia.valueChanged['int'].connect(self.lcdNumber_Reverb_Ganancia.display) # type: ignore
        self.verticalSlider_Echo_Retraso.valueChanged['int'].connect(self.lcdNumber_Echo_Retraso.display) # type: ignore
        self.verticalSlider_Flanger_Ganancia.valueChanged['int'].connect(self.lcdNumber_Flanger_Ganancia.display) # type: ignore
        self.verticalSlider_Echo_Ganancia.valueChanged['int'].connect(self.lcdNumber_Echo_Ganancia.display) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Form"))
        self.label.setText(_translate("Menu", "ASSD - TP2 - GRUPO 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Menu", "Presentaci??n"))
        self.pushButton_Upload.setText(_translate("Menu", "UPLOAD"))
        self.pushButton_Save.setText(_translate("Menu", "SAVE"))
        self.label_track0.setText(_translate("Menu", "Track 0"))
        self.comboBox_track0.setItemText(0, _translate("Menu", "Piano"))
        self.comboBox_track0.setItemText(1, _translate("Menu", "Flauta"))
        self.comboBox_track0.setItemText(2, _translate("Menu", "Guitarra Electrica"))
        self.comboBox_track0.setItemText(3, _translate("Menu", "Tambores"))
        self.pushButton_mute_track0.setText(_translate("Menu", "Mute"))
        self.pushButton_Sintetizar.setText(_translate("Menu", "SINTETIZAR"))
        self.checkBox_Reverb.setText(_translate("Menu", "Reverb"))
        self.label_15.setText(_translate("Menu", "Retraso [ms]"))
        self.label_16.setText(_translate("Menu", "Ganancia [%]"))
        self.checkBox_Echo.setText(_translate("Menu", "Echo"))
        self.label_10.setText(_translate("Menu", "Retraso [ms]"))
        self.label_11.setText(_translate("Menu", "Ganancia [%]"))
        self.checkBox_Flanger.setText(_translate("Menu", "Flanger"))
        self.label_12.setText(_translate("Menu", "Retraso [ms]"))
        self.label_13.setText(_translate("Menu", "Frecuencia [Hz]"))
        self.label_14.setText(_translate("Menu", "Ganancia [%]"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Menu", "Sintetizador"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Menu = QtWidgets.QWidget()
    ui = Ui_Menu()
    ui.setupUi(Menu)
    Menu.show()
    sys.exit(app.exec_())
