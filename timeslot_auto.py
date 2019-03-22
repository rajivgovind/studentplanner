# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timeslot.ui'
#
# Created: Fri Mar 22 13:03:15 2019
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
        Dialog.resize(315, 75)
        self.btn_done = QtGui.QPushButton(Dialog)
        self.btn_done.setGeometry(QtCore.QRect(170, 40, 111, 23))
        self.btn_done.setObjectName(_fromUtf8("btn_done"))
        self.lbl_timeinterval = QtGui.QLabel(Dialog)
        self.lbl_timeinterval.setGeometry(QtCore.QRect(20, 0, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_timeinterval.setFont(font)
        self.lbl_timeinterval.setObjectName(_fromUtf8("lbl_timeinterval"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lne_interval = QtGui.QLineEdit(Dialog)
        self.lne_interval.setGeometry(QtCore.QRect(160, 10, 131, 20))
        self.lne_interval.setObjectName(_fromUtf8("lne_interval"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.btn_done, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Time Slot", None))
        self.btn_done.setText(_translate("Dialog", "Done", None))
        self.lbl_timeinterval.setText(_translate("Dialog", "Enter Time Interval", None))
        self.label.setText(_translate("Dialog", "Enter in the format:", None))
        self.label_2.setText(_translate("Dialog", "HH:MM - HH:MM", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

