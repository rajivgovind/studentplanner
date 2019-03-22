# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calendar.ui'
#
# Created: Fri Mar 22 13:02:32 2019
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
        Dialog.resize(371, 295)
        self.calendarWidget = QtGui.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 20, 331, 221))
        self.calendarWidget.setStyleSheet(_fromUtf8("font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(40, 192, 200);\n"
"color: rgb(0, 0, 0);"))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.btn_submit = QtGui.QPushButton(Dialog)
        self.btn_submit.setGeometry(QtCore.QRect(110, 250, 144, 31))
        self.btn_submit.setObjectName(_fromUtf8("btn_submit"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.btn_submit, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Calendar", None))
        self.btn_submit.setText(_translate("Dialog", "Submit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

