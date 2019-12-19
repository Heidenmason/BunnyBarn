import sqlite3
import sys
from PyQt5 import QtWidgets, QtGui

# from PyQt5.QtGui import QPixmap
from main_window import *  # importing our generated file

data = ['PyQt5', 'Is']


#  \b(todo)\b.*

class Main(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.statusbar = self.statusBar()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.title = "Heiden APP"  # Sets window title
        self.setWindowTitle(self.title)  # Sets window title
        # self.statusBar().showMessage("Message in lower statusbar.")

        self.initwindow()

    def initwindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))  # Sets Start Bar Icon
        # self.statusBar().showMessage("Message in statusbar.")
        self.statusbar.showMessage('Ready')

        # label to image
        mypixmap = QtGui.QPixmap('image.jpg')
        self.ui.label.setPixmap(mypixmap)
        self.ui.label.resize(mypixmap.width(), mypixmap.height())
        self.ui.label.resize(126, 180)  # portrait
        # self.ui.label.resize(180,110) #landscape
        myscaledpixmap = mypixmap.scaled(self.ui.label.size())
        self.ui.label.setPixmap(myscaledpixmap)
        # label to image.


app = QtWidgets.QApplication([])
application = Main()
application.show()  # IMPORTANT!!!!! Windows are hidden by default.
sys.exit(app.exec())  # Start the event loop.

# Application won't reach here until you exit and the event
# loop has stopped.

# Build Files
# From file directory
# convert .ui file to .py file. &&-if successful open file

# pyuic5 main_window.ui -o main_window.py && python3 main.py

# generate one executable file
# pyinstaller --onefile main.py
