from PyQt5 import QtCore, QtGui, QtWidgets
import asset.suggestionUI as Suggestion
import sys

class Ui_startWindow(object):
    def setupUi(self, startWindow):
        startWindow.setObjectName("startWindow")
        startWindow.resize(300, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(startWindow.sizePolicy().hasHeightForWidth())
        startWindow.setSizePolicy(sizePolicy)
        startWindow.setMaximumSize(QtCore.QSize(300, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("config/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("config/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        startWindow.setWindowIcon(icon)
        font = QtGui.QFont()
        font.setPointSize(10)
        startWindow.setFont(font)
        self.logoLabel = QtWidgets.QLabel(startWindow)
        self.logoLabel.setGeometry(QtCore.QRect(5, 0, 290, 370))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logoLabel.sizePolicy().hasHeightForWidth())
        self.logoLabel.setSizePolicy(sizePolicy)
        self.logoLabel.setObjectName("logoLabel")

        self.startButton = QtWidgets.QPushButton(startWindow)
        self.startButton.setGeometry(QtCore.QRect(15, 370, 120, 25))
        self.startButton.setObjectName("startButton")
        self.startButton.clicked.connect(self.clicked_startButton)
        self.thisWindow = startWindow

        self.closeButton = QtWidgets.QPushButton(startWindow)
        self.closeButton.setGeometry(QtCore.QRect(160, 370, 120, 25))
        self.closeButton.setObjectName("closeButton")
        self.closeButton.clicked.connect(self.clicked_closeButton)

        self.retranslateUi(startWindow)
        QtCore.QMetaObject.connectSlotsByName(startWindow)

    def retranslateUi(self, startWindow):
        _translate = QtCore.QCoreApplication.translate
        startWindow.setWindowTitle(_translate("startWindow", "Senior Design by Jonathan Chua"))
        self.logoLabel.setText(_translate("startWindow", "<html><head/><body><p><img src=\"./config/banner.jpg\"/></p></body></html>"))
        self.startButton.setText(_translate("startWindow", "Start Program"))
        self.closeButton.setText(_translate("startWindow", "Close Program"))

    def clicked_closeButton(self):
        sys.exit()

    def clicked_startButton(self):
        '''
        Description: method instantiates the suggestionUI and then shows the suggestion window while hiding the start window.
        '''
        self.suggestion = Suggestion.Ui_suggestionWindow()
        self.suggestionWindow = QtWidgets.QDialog()
        self.suggestion.setupUi(self.suggestionWindow)
        self.suggestionWindow.show()
        self.thisWindow.hide()