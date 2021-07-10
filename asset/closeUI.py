from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import sys

class Ui_closeWindow(object):
    def setupUi(self, closeWindow):
        closeWindow.setObjectName("closeWindow")
        closeWindow.resize(360, 240)
        closeWindow.setMaximumSize(QtCore.QSize(360, 240))
        self.centralwidget = QtWidgets.QWidget(closeWindow)
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.closeButton = QtWidgets.QPushButton(closeWindow)
        self.closeButton.setGeometry(QtCore.QRect(120, 210, 120, 25))
        self.closeButton.setObjectName("pushButton")
        self.closeButton.clicked.connect(self.clicked_closeButton)

        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(0, 0, 360, 202))
        self.logo.setMinimumSize(QtCore.QSize(360, 202))
        self.logo.setMaximumSize(QtCore.QSize(360, 202))
        self.logo.setObjectName("logo")

        closeWindow.setCentralWidget(self.centralwidget)

        self.movie = QMovie("./config/welcome.gif")
        self.logo.setMovie(self.movie)
        self.movie.start()

        self.retranslateUi(closeWindow)
        QtCore.QMetaObject.connectSlotsByName(closeWindow)

    def retranslateUi(self, closeWindow):
        _translate = QtCore.QCoreApplication.translate
        closeWindow.setWindowTitle(_translate("closeWindow", "You\'re welcome!"))
        self.closeButton.setText(_translate("closeWindow", "Close Program"))

    def clicked_closeButton(self):
        sys.exit()