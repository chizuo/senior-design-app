from PyQt5 import QtWidgets
import asset.startUI as Main

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    startWindow = QtWidgets.QDialog()
    ui = Main.Ui_startWindow()
    ui.setupUi(startWindow)
    startWindow.show()
    sys.exit(app.exec_())