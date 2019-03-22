# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created: Fri Mar 22 12:57:56 2019
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(584, 416)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lbl_planner = QtGui.QLabel(self.centralwidget)
        self.lbl_planner.setGeometry(QtCore.QRect(180, 0, 271, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_planner.setFont(font)
        self.lbl_planner.setObjectName(_fromUtf8("lbl_planner"))
        self.cal_date = QtGui.QCalendarWidget(self.centralwidget)
        self.cal_date.setGeometry(QtCore.QRect(20, 80, 281, 281))
        self.cal_date.setObjectName(_fromUtf8("cal_date"))
        self.lw_selectedDate = QtGui.QListWidget(self.centralwidget)
        self.lw_selectedDate.setGeometry(QtCore.QRect(320, 100, 241, 81))
        self.lw_selectedDate.setObjectName(_fromUtf8("lw_selectedDate"))
        self.lw_events = QtGui.QListWidget(self.centralwidget)
        self.lw_events.setGeometry(QtCore.QRect(320, 210, 241, 151))
        self.lw_events.setObjectName(_fromUtf8("lw_events"))
        self.lbl_username = QtGui.QLabel(self.centralwidget)
        self.lbl_username.setGeometry(QtCore.QRect(380, 180, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_username.setFont(font)
        self.lbl_username.setObjectName(_fromUtf8("lbl_username"))
        self.lbl_username_2 = QtGui.QLabel(self.centralwidget)
        self.lbl_username_2.setGeometry(QtCore.QRect(360, 70, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_username_2.setFont(font)
        self.lbl_username_2.setObjectName(_fromUtf8("lbl_username_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 584, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuToolbar = QtGui.QMenu(self.menubar)
        self.menuToolbar.setObjectName(_fromUtf8("menuToolbar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionTasks = QtGui.QAction(MainWindow)
        self.actionTasks.setObjectName(_fromUtf8("actionTasks"))
        self.actionScheduling = QtGui.QAction(MainWindow)
        self.actionScheduling.setObjectName(_fromUtf8("actionScheduling"))
        self.actionLog_out = QtGui.QAction(MainWindow)
        self.actionLog_out.setObjectName(_fromUtf8("actionLog_out"))
        self.menuToolbar.addAction(self.actionTasks)
        self.menuToolbar.addAction(self.actionScheduling)
        self.menuToolbar.addAction(self.actionLog_out)
        self.menubar.addAction(self.menuToolbar.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.lbl_planner.setText(_translate("MainWindow", "Student Planner", None))
        self.lbl_username.setText(_translate("MainWindow", "Upcoming Events", None))
        self.lbl_username_2.setText(_translate("MainWindow", "Tasks on Selected Date", None))
        self.menuToolbar.setTitle(_translate("MainWindow", "Toolbar", None))
        self.actionTasks.setText(_translate("MainWindow", "Tasks", None))
        self.actionScheduling.setText(_translate("MainWindow", "Scheduling", None))
        self.actionLog_out.setText(_translate("MainWindow", "Log out", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

