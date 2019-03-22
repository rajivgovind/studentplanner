# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created: Fri Mar 22 13:02:59 2019
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
        Dialog.resize(302, 175)
        self.lbl_username = QtGui.QLabel(Dialog)
        self.lbl_username.setGeometry(QtCore.QRect(30, 20, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_username.setFont(font)
        self.lbl_username.setObjectName(_fromUtf8("lbl_username"))
        self.lbl_confirm = QtGui.QLabel(Dialog)
        self.lbl_confirm.setGeometry(QtCore.QRect(30, 100, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_confirm.setFont(font)
        self.lbl_confirm.setObjectName(_fromUtf8("lbl_confirm"))
        self.lbl_password = QtGui.QLabel(Dialog)
        self.lbl_password.setGeometry(QtCore.QRect(30, 60, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_password.setFont(font)
        self.lbl_password.setObjectName(_fromUtf8("lbl_password"))
        self.lne_username = QtGui.QLineEdit(Dialog)
        self.lne_username.setGeometry(QtCore.QRect(160, 20, 113, 20))
        self.lne_username.setObjectName(_fromUtf8("lne_username"))
        self.lne_password = QtGui.QLineEdit(Dialog)
        self.lne_password.setGeometry(QtCore.QRect(160, 60, 113, 20))
        self.lne_password.setObjectName(_fromUtf8("lne_password"))
        self.lne_confirm = QtGui.QLineEdit(Dialog)
        self.lne_confirm.setGeometry(QtCore.QRect(160, 100, 113, 20))
        self.lne_confirm.setObjectName(_fromUtf8("lne_confirm"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 140, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lbl_username.setText(_translate("Dialog", "Username", None))
        self.lbl_confirm.setText(_translate("Dialog", "Confirm Password", None))
        self.lbl_password.setText(_translate("Dialog", "Password", None))
        self.pushButton.setText(_translate("Dialog", "Done", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

