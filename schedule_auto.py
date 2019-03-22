# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'schedule.ui'
#
# Created: Fri Mar 22 13:02:44 2019
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(497, 292)
        self.lw_free = QtGui.QListWidget(Dialog)
        self.lw_free.setGeometry(QtCore.QRect(10, 50, 121, 192))
        self.lw_free.setObjectName(_fromUtf8("lw_free"))
        self.lw_time = QtGui.QListWidget(Dialog)
        self.lw_time.setGeometry(QtCore.QRect(170, 50, 111, 192))
        self.lw_time.setObjectName(_fromUtf8("lw_time"))
        self.lbl_free = QtGui.QLabel(Dialog)
        self.lbl_free.setGeometry(QtCore.QRect(30, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_free.setFont(font)
        self.lbl_free.setObjectName(_fromUtf8("lbl_free"))
        self.lbl_time = QtGui.QLabel(Dialog)
        self.lbl_time.setGeometry(QtCore.QRect(180, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_time.setFont(font)
        self.lbl_time.setObjectName(_fromUtf8("lbl_time"))
        self.lbl_task = QtGui.QLabel(Dialog)
        self.lbl_task.setGeometry(QtCore.QRect(370, 10, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_task.setFont(font)
        self.lbl_task.setObjectName(_fromUtf8("lbl_task"))
        self.lw_task = QtGui.QListWidget(Dialog)
        self.lw_task.setGeometry(QtCore.QRect(310, 50, 171, 192))
        self.lw_task.setObjectName(_fromUtf8("lw_task"))
        self.btn_add = QtGui.QPushButton(Dialog)
        self.btn_add.setGeometry(QtCore.QRect(10, 250, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btn_add.setFont(font)
        self.btn_add.setObjectName(_fromUtf8("btn_add"))
        self.btn_process = QtGui.QPushButton(Dialog)
        self.btn_process.setGeometry(QtCore.QRect(170, 250, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btn_process.setFont(font)
        self.btn_process.setObjectName(_fromUtf8("btn_process"))
        self.lbl_message = QtGui.QLabel(Dialog)
        self.lbl_message.setGeometry(QtCore.QRect(310, 250, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_message.setFont(font)
        self.lbl_message.setObjectName(_fromUtf8("lbl_message"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(370, 270, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Schedule", None))
        self.lbl_free.setText(_translate("Dialog", "Free Time", None))
        self.lbl_time.setText(_translate("Dialog", "Time Period", None))
        self.lbl_task.setText(_translate("Dialog", "Task", None))
        self.btn_add.setText(_translate("Dialog", "Add Free Time", None))
        self.btn_process.setText(_translate("Dialog", "Process", None))
        self.lbl_message.setText(_translate("Dialog", "*Only click when done finalising", None))
        self.label.setText(_translate("Dialog", "free time", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

