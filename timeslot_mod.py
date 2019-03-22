import sys
from PyQt4 import QtCore, QtGui, uic
import sqlite3
from timeslot_auto import *
class MyWindowClass(QtGui.QMainWindow, Ui_MainWindow):
 def __init__(self, parent=None):
     QtGui.QMainWindow.__init__(self, parent)
     self.setupUi(self)
     #self.connect(self.actionCode,QtCore.SIGNAL("triggered()"),self.code)



app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()

