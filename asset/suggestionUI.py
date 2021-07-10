from PyQt5 import QtCore, QtWidgets
from asset.imdb import ImdbApi
from asset.user import AppHash
from asset.dbalapi import RestApi
import asset.movieUI as Movie
import sys
import config.imdb as imdb

class Ui_suggestionWindow(object):
    def setupUi(self, suggestionWindow):
        suggestionWindow.setObjectName("suggestionWindow")
        suggestionWindow.resize(480, 320)
        suggestionWindow.setMaximumSize(QtCore.QSize(480, 320))
        self.thisWindow = suggestionWindow
        self.credentials = RestApi.GET_User(AppHash().hashedID)
        print(self.credentials)
        
        self.suggestLogo = QtWidgets.QLabel(suggestionWindow)
        self.suggestLogo.setGeometry(QtCore.QRect(10, 10, 224, 270))
        self.suggestLogo.setObjectName("suggestLogo")
        
        self.randomButton = QtWidgets.QPushButton(suggestionWindow)
        self.randomButton.setGeometry(QtCore.QRect(240, 10, 230, 60))
        self.randomButton.setObjectName("randomButton")
        self.randomButton.clicked.connect(self.clicked_randomButton)
        
        self.trendyButton = QtWidgets.QPushButton(suggestionWindow)
        self.trendyButton.setGeometry(QtCore.QRect(240, 80, 230, 60))
        self.trendyButton.setObjectName("trendyButton")
        self.trendyButton.clicked.connect(self.clicked_trendyButton)
        
        self.nowButton = QtWidgets.QPushButton(suggestionWindow)
        self.nowButton.setGeometry(QtCore.QRect(240, 150, 230, 60))
        self.nowButton.setObjectName("nowButton")
        self.nowButton.clicked.connect(self.clicked_nowButton)
        
        self.savedButton = QtWidgets.QPushButton(suggestionWindow)
        self.savedButton.setGeometry(QtCore.QRect(240, 220, 230, 60))
        self.savedButton.setObjectName("savedButton")
        self.savedButton.clicked.connect(self.clicked_savedButton)
        
        self.closeButton = QtWidgets.QPushButton(suggestionWindow)
        self.closeButton.setGeometry(QtCore.QRect(180, 290, 120, 25))
        self.closeButton.setObjectName("closeButton")
        self.closeButton.clicked.connect(self.clicked_closeButton)

        self.retranslateUi(suggestionWindow)
        QtCore.QMetaObject.connectSlotsByName(suggestionWindow)

    def retranslateUi(self, suggestionWindow):
        _translate = QtCore.QCoreApplication.translate
        suggestionWindow.setWindowTitle(_translate("suggestionWindow", "Go Ahead, Make my Movie Night by Jonathan Chua"))
        self.suggestLogo.setText(_translate("suggestionWindow", "<html><head/><body><p><img src=\"./config/suggestion.png\"/></p></body></html>"))
        self.randomButton.setText(_translate("suggestionWindow", "Completely Random Movies"))
        self.trendyButton.setText(_translate("suggestionWindow", "Movies Currently Trending"))
        self.nowButton.setText(_translate("suggestionWindow", "Movies Currently in Theaters"))
        self.savedButton.setText(_translate("suggestionWindow", "Suggest from my Saved List"))
        self.closeButton.setText(_translate("suggestionWindow", "Close Program"))

    def clicked_closeButton(self):
        sys.exit()

    def clicked_randomButton(self):
        self.launch_movieUI(ImdbApi().make_request(imdb.random, 1), imdb.random)

    def clicked_trendyButton(self):
        self.launch_movieUI(ImdbApi().make_request(imdb.trending, 1), imdb.trending)

    def clicked_nowButton(self):
        self.launch_movieUI(ImdbApi().make_request(imdb.nowPlaying, 1), imdb.nowPlaying)
    
    def clicked_savedButton(self):
        self.launch_movieUI(RestApi.GET_Movie(self.credentials), 'fromSaved')

    def launch_movieUI(self, movieList, typeCall):
        '''
        Description: instantiates the movieUI and passes the results of the 1st list of 20 suggestion of that movie category chosen by the user.
        Receives: list of movies that are JSON objects, string containing the category used for the ImdbApi call.
        '''
        self.movie = Movie.Ui_movieWindow()
        self.movieWindow = QtWidgets.QDialog()
        self.movie.setupUi(self.movieWindow, self.thisWindow, movieList, typeCall, 1, self.credentials)
        self.movieWindow.show()
        self.thisWindow.close()