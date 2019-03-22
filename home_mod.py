import sys
from PyQt4 import QtCore, QtGui, uic
import sqlite3
import tasks_mod
import schedule_mod
import signin_mod
from home_auto import *
class MyWindowClass(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.connect(self.actionTasks,QtCore.SIGNAL("triggered()"),self.tasks)
        self.connect(self.actionScheduling,QtCore.SIGNAL("triggered()"),self.schedule)
        self.connect(self.actionLog_out,QtCore.SIGNAL("triggered()"),self.logout)
        
    def tasks(self):
             tasks = tasks_mod.MyForm(self)
             tasks.exec()

    def schedule(self):
             schedule = schedule_mod.MyForm(self)
             schedule.exec()

    def logout(self):
             logout = signin_mod.MyForm(self)
             logout.exec()

app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()
