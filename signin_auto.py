# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signin.ui'
#
# Created: Fri Mar 22 13:02:53 2019
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
        Dialog.resize(325, 169)
        self.lbl_username = QtGui.QLabel(Dialog)
        self.lbl_username.setGeometry(QtCore.QRect(40, 30, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_username.setFont(font)
        self.lbl_username.setObjectName(_fromUtf8("lbl_username"))
        self.lbl_password = QtGui.QLabel(Dialog)
        self.lbl_password.setGeometry(QtCore.QRect(40, 80, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_password.setFont(font)
        self.lbl_password.setObjectName(_fromUtf8("lbl_password"))
        self.lne_username = QtGui.QLineEdit(Dialog)
        self.lne_username.setGeometry(QtCore.QRect(160, 30, 113, 20))
        self.lne_username.setObjectName(_fromUtf8("lne_username"))
        self.lne_password = QtGui.QLineEdit(Dialog)
        self.lne_password.setGeometry(QtCore.QRect(160, 80, 113, 20))
        self.lne_password.setObjectName(_fromUtf8("lne_password"))
        self.btn_login = QtGui.QPushButton(Dialog)
        self.btn_login.setGeometry(QtCore.QRect(40, 120, 91, 21))
        self.btn_login.setObjectName(_fromUtf8("btn_login"))
        self.btn_signup = QtGui.QPushButton(Dialog)
        self.btn_signup.setGeometry(QtCore.QRect(174, 120, 91, 23))
        self.btn_signup.setObjectName(_fromUtf8("btn_signup"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.btn_login, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lbl_username.setText(_translate("Dialog", "Username", None))
        self.lbl_password.setText(_translate("Dialog", "Password", None))
        self.btn_login.setText(_translate("Dialog", "Log in", None))
        self.btn_signup.setText(_translate("Dialog", "Sign Up", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

