from asset.imdb import ImdbApi
from asset.dbalapi import RestApi
from asset.movie import Movie
from PyQt5 import QtCore, QtGui, QtWidgets
import asset.closeUI as Close
import json

class Ui_movieWindow(object):
    def setupUi(self, movieWindow, suggestionWindow, movieList, typeCall, atPage, credentials):
        movieWindow.setObjectName("movieWindow")
        movieWindow.resize(600, 800)
        movieWindow.setMaximumSize(QtCore.QSize(600, 800))
        font = QtGui.QFont()
        font.setPointSize(12)
        movieWindow.setFont(font)

        #attributes to the current movieWindow with the particular button criteria used in the suggestionsWindow
        self.thisWindow = movieWindow
        self.prevWindow = suggestionWindow
        self.movieList = movieList
        self.atPage = atPage
        self.typeCall = typeCall
        self.id = credentials

        self.titleLabel = QtWidgets.QLabel(movieWindow)
        self.titleLabel.setGeometry(QtCore.QRect(240, 320, 40, 20))
        self.titleLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.titleLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.titleLabel.setObjectName("titleLabel")
        self.logoLabel = QtWidgets.QLabel(movieWindow)
        self.logoLabel.setGeometry(QtCore.QRect(2, 4, 600, 290))
        self.logoLabel.setObjectName("logoLabel")
        self.genreLabel = QtWidgets.QLabel(movieWindow)
        self.genreLabel.setGeometry(QtCore.QRect(480, 410, 50, 20))
        self.genreLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.genreLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.genreLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.genreLabel.setObjectName("genreLabel")
        self.yearLabel = QtWidgets.QLabel(movieWindow)
        self.yearLabel.setGeometry(QtCore.QRect(425, 380, 40, 20))
        self.yearLabel.setObjectName("yearLabel")
        self.ratingLabel = QtWidgets.QLabel(movieWindow)
        self.ratingLabel.setGeometry(QtCore.QRect(240, 380, 50, 20))
        self.ratingLabel.setObjectName("ratingLabel")
        self.ratedLabel = QtWidgets.QLabel(movieWindow)
        self.ratedLabel.setGeometry(QtCore.QRect(240, 350, 50, 20))
        self.ratedLabel.setObjectName("ratedLabel")
        self.lengthLabel = QtWidgets.QLabel(movieWindow)
        self.lengthLabel.setGeometry(QtCore.QRect(400, 350, 70, 20))
        self.lengthLabel.setObjectName("lengthLabel")
        self.languageLabel = QtWidgets.QLabel(movieWindow)
        self.languageLabel.setGeometry(QtCore.QRect(280, 410, 80, 20))
        self.languageLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.languageLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.languageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.languageLabel.setObjectName("languageLabel")
        self.actorLabel = QtWidgets.QLabel(movieWindow)
        self.actorLabel.setGeometry(QtCore.QRect(80, 300, 80, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actorLabel.setFont(font)
        self.actorLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.actorLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.actorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.actorLabel.setObjectName("actorLabel")
        self.directorLabel = QtWidgets.QLabel(movieWindow)
        self.directorLabel.setGeometry(QtCore.QRect(80, 600, 80, 20))
        self.directorLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.directorLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.directorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.directorLabel.setObjectName("directorLabel")
        self.descriptLabel = QtWidgets.QLabel(movieWindow)
        self.descriptLabel.setGeometry(QtCore.QRect(350, 520, 125, 20))
        self.descriptLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.descriptLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.descriptLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.descriptLabel.setObjectName("descriptLabel")
        self.actorList = QtWidgets.QListWidget(movieWindow)
        self.actorList.setGeometry(QtCore.QRect(10, 320, 220, 270))
        self.actorList.setObjectName("actorList")
        self.filmText = QtWidgets.QTextEdit(movieWindow)
        self.filmText.setGeometry(QtCore.QRect(240, 540, 350, 210))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filmText.sizePolicy().hasHeightForWidth())    
        self.filmText.setSizePolicy(sizePolicy)
        self.filmText.setMaximumSize(QtCore.QSize(350, 220))
        self.filmText.setObjectName("filmText")
        self.titleText = QtWidgets.QTextEdit(movieWindow)
        self.titleText.setGeometry(QtCore.QRect(280, 315, 310, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleText.sizePolicy().hasHeightForWidth())
        self.titleText.setSizePolicy(sizePolicy)
        self.titleText.setMaximumSize(QtCore.QSize(310, 25))
        self.titleText.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.titleText.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.titleText.setObjectName("titleText")
        self.ratedText = QtWidgets.QTextEdit(movieWindow)
        self.ratedText.setGeometry(QtCore.QRect(290, 345, 100, 25))
        self.ratedText.setMaximumSize(QtCore.QSize(100, 25))
        self.ratedText.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.ratedText.setObjectName("ratedText")        
        self.runtimeText = QtWidgets.QTextEdit(movieWindow)
        self.runtimeText.setGeometry(QtCore.QRect(470, 345, 120, 25))
        self.runtimeText.setObjectName("runtimeText")
        self.ratingText = QtWidgets.QTextEdit(movieWindow)
        self.ratingText.setGeometry(QtCore.QRect(290, 375, 100, 25))
        self.ratingText.setObjectName("ratingText")
        self.yearText = QtWidgets.QTextEdit(movieWindow)
        self.yearText.setGeometry(QtCore.QRect(470, 375, 120, 25))
        self.yearText.setObjectName("yearText")
        self.directorList = QtWidgets.QListWidget(movieWindow)
        self.directorList.setGeometry(QtCore.QRect(10, 620, 220, 130))
        self.directorList.setObjectName("directorList")
        self.langList = QtWidgets.QListWidget(movieWindow)
        self.langList.setGeometry(QtCore.QRect(240, 430, 170, 80))
        self.langList.setObjectName("langList")
        self.genreList = QtWidgets.QListWidget(movieWindow)
        self.genreList.setGeometry(QtCore.QRect(419, 430, 170, 80))
        self.genreList.setObjectName("genreList")

        self.acceptButton = QtWidgets.QPushButton(movieWindow)
        self.acceptButton.setGeometry(QtCore.QRect(10, 760, 140, 25))
        self.acceptButton.setObjectName("acceptButton")
        self.acceptButton.clicked.connect(self.clicked_acceptButton)
        
        self.saveButton = QtWidgets.QPushButton(movieWindow)
        self.saveButton.setGeometry(QtCore.QRect(150, 760, 140, 25))
        self.saveButton.setObjectName("saveButton")
        self.saveButton.clicked.connect(self.clicked_saveButton)
        
        self.passButton = QtWidgets.QPushButton(movieWindow)
        self.passButton.setGeometry(QtCore.QRect(290, 760, 150, 25))
        self.passButton.setObjectName("passButton")
        self.passButton.clicked.connect(self.clicked_passButton)
        
        self.optionsButton = QtWidgets.QPushButton(movieWindow)
        self.optionsButton.setGeometry(QtCore.QRect(440, 760, 150, 25))
        self.optionsButton.setObjectName("optionsButton")
        self.optionsButton.clicked.connect(self.clicked_optionsButton)

        self.retranslateUi(movieWindow)
        QtCore.QMetaObject.connectSlotsByName(movieWindow)

        if(typeCall == 'fromSaved'):
            self.unpackSaved()
        else:
            self.unpack()

    def retranslateUi(self, movieWindow):
        _translate = QtCore.QCoreApplication.translate
        movieWindow.setWindowTitle(_translate("movieWindow", "Go Ahead, Make my Movie Night by Jonathan Chua"))
        self.titleLabel.setText(_translate("movieWindow", "Title:"))
        self.logoLabel.setText(_translate("movieWindow", "<html><head/><body><p><img src=\"./config/movieUI.jpg\"/></p></body></html>"))
        self.genreLabel.setText(_translate("movieWindow", "Genre"))
        self.yearLabel.setText(_translate("movieWindow", "Year :"))
        self.ratingLabel.setText(_translate("movieWindow", "Score :"))
        self.ratedLabel.setText(_translate("movieWindow", "Rated:"))
        self.lengthLabel.setText(_translate("movieWindow", "Runtime:"))
        self.languageLabel.setText(_translate("movieWindow", "Language"))
        self.actorLabel.setText(_translate("movieWindow", "Starring"))
        self.directorLabel.setText(_translate("movieWindow", "Director"))
        self.optionsButton.setText(_translate("movieWindow", "Back to options"))
        self.descriptLabel.setText(_translate("movieWindow", "Film Description"))
        self.acceptButton.setText(_translate("movieWindow", "Will watch now!"))
        self.saveButton.setText(_translate("movieWindow", "Save this for later"))
        self.passButton.setText(_translate("movieWindow", "Pass, next!"))

    def clicked_acceptButton(self):
        '''
        Description: this method records the movie details to a file that contains all movies the user has stated to watch as a datapoint and then
        instantiates and shows the closeUI before hiding the movieUI.
        '''
        watchFile = open('./config/watched.txt','a')
        watchFile.write(self.enter_datapoint())
        watchFile.close()
        self.closeWindow = QtWidgets.QMainWindow()
        self.close = Close.Ui_closeWindow()
        self.close.setupUi(self.closeWindow)
        self.closeWindow.show()
        self.thisWindow.hide()

    def clicked_optionsButton(self):
        '''
        Description: this method will close this instance of the movieUI and reopens the suggestionUI.
        '''
        self.prevWindow.show()
        self.thisWindow.close()
    
    def clicked_passButton(self):
        '''
        Description: this method records the movie details to a fail that contains all moves the user has stated disinterest in while also unpacking the
        next movie movie suggestion.
        '''
        passFile = open('./config/passed.txt','a')
        passFile.write(self.enter_datapoint())
        passFile.close()
        if(self.typeCall == 'fromSaved'):
            self.movieList = RestApi.GET_Movie(self.id)
            self.unpackSaved()
        else:
            self.unpack()

    def clicked_saveButton(self):
        '''
        Description: this method makes a POST request to the REST API of this project's DBAL Web Service to save this particular suggestion in the database.
        '''
        RestApi.POST_Movie(self.id, self.movie.id)
        if(self.typeCall == 'fromSaved'):
            self.movieList = RestApi.GET_Movie(self.id)
            self.unpackSaved()
        else:
            self.unpack()

    def clear_lists(self):
        '''
        Description: this method clears the list views of the UI. Which is used whenever the update method is called.
        '''
        self.langList.clear()
        self.genreList.clear()
        self.actorList.clear()
        self.directorList.clear()

    def enter_datapoint(self):
        '''
        Description: this method formats the movie to a parsable format with delimiters
        '''
        datapoint = '#start_datapoint#\n'
        if(self.movie.title):
            datapoint += 'title:' + self.movie.title + '\n'
        else:
            datapoint += 'title:None Provided\n'

        if(self.movie.rated):
            datapoint += 'rated:' + self.movie.rated + '\n'
        else:
            datapoint += 'rated:None Provided\n'
        
        if(self.movie.genres):
            datapoint += 'genres:'
            for genre in self.movie.genres:
                datapoint += '[' + genre + ']'
            datapoint += '\n'
        else:
            datapoint += 'genres:None Provided\n' 

        if(self.movie.actors):
            datapoint += 'starring:'
            for actor in self.movie.actors:
                datapoint += '[' + actor + ']'
            datapoint += '\n'
        else:
            datapoint += 'starring:None Provided\n'

        if(self.movie.directors):
            datapoint += 'director:' + self.movie.directors[0] + '\n'
        else:
            datapoint += 'director:None Provided\n'
        datapoint+= '#end_datapoint#\n'
        return datapoint

    def unpack(self):
        '''
        Description: this method converts the return of the ImdbApi request to a format which can be understood by the Movie class.
        The movie object that is instantiated is then passed to the update method to show the details of this movie suggestion.
        '''
        if(len(self.movieList) > 0):
            result = self.movieList.pop(0)
            kv = ImdbApi().movie_details(result["imdb_id"])
            self.movie = Movie(kv["title"],kv["description"],kv["year"],kv["imdb_id"],kv["imdb_rating"],kv["rated"],kv["runtime"],kv["genres"],kv["stars"],kv["directors"],kv["language"])
            self.update(self.movie)
        else:
            print("Type: %s @ Page: %i" %(self.typeCall, self.atPage))
            self.atPage = self.atPage + 1
            self.movieList = ImdbApi().make_request(self.typeCall, self.atPage)
            self.unpack()

    def unpackSaved(self):
        """
        Description: this method converts the return of the REST API request to a format which can be understood by the Movie class.
        The movie object that is instantiated is then passed to the update method to show the details of this movie suggestion.
        """
        kv = ImdbApi().movie_details(self.movieList)
        self.movie = Movie(kv["title"],kv["description"],kv["year"],kv["imdb_id"],kv["imdb_rating"],kv["rated"],kv["runtime"],kv["genres"],kv["stars"],kv["directors"],kv["language"])
        self.update(self.movie)
        RestApi.DELETE_Movie(self.id, self.movie.id)

    def update(self, movie):
        '''
        Description: this method updates the UI to populate the movie that was suggested.
        '''
        self.clear_lists()
        self.titleText.setText(movie.title)
        self.filmText.setText(movie.description)
        self.yearText.setText(movie.year)
        self.ratingText.setText(movie.rating)
        self.ratedText.setText(movie.rated)
        self.runtimeText.setText(str(movie.runtime))
        
        if(movie.language):
            self.langList.addItems(movie.language)
        
        if(movie.genres):
            self.genreList.addItems(movie.genres)
        
        if(movie.directors):
            self.directorList.addItems(movie.directors)
 
        if(movie.actors):
            self.actorList.addItems(movie.actors)