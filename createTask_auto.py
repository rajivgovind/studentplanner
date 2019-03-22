# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createTask.ui'
#
# Created: Fri Mar 22 13:02:10 2019
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
        Dialog.resize(545, 292)
        self.lbl_activities = QtGui.QLabel(Dialog)
        self.lbl_activities.setGeometry(QtCore.QRect(50, 20, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_activities.setFont(font)
        self.lbl_activities.setObjectName(_fromUtf8("lbl_activities"))
        self.tv_data = QtGui.QTableView(Dialog)
        self.tv_data.setGeometry(QtCore.QRect(20, 50, 181, 201))
        self.tv_data.setObjectName(_fromUtf8("tv_data"))
        self.lbl_assignedBy = QtGui.QLabel(Dialog)
        self.lbl_assignedBy.setGeometry(QtCore.QRect(220, 90, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_assignedBy.setFont(font)
        self.lbl_assignedBy.setObjectName(_fromUtf8("lbl_assignedBy"))
        self.lbl_startDate = QtGui.QLabel(Dialog)
        self.lbl_startDate.setGeometry(QtCore.QRect(220, 180, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_startDate.setFont(font)
        self.lbl_startDate.setObjectName(_fromUtf8("lbl_startDate"))
        self.lbl_taskName = QtGui.QLabel(Dialog)
        self.lbl_taskName.setGeometry(QtCore.QRect(220, 60, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_taskName.setFont(font)
        self.lbl_taskName.setObjectName(_fromUtf8("lbl_taskName"))
        self.lbl_duration = QtGui.QLabel(Dialog)
        self.lbl_duration.setGeometry(QtCore.QRect(220, 130, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_duration.setFont(font)
        self.lbl_duration.setObjectName(_fromUtf8("lbl_duration"))
        self.lbl_priority = QtGui.QLabel(Dialog)
        self.lbl_priority.setGeometry(QtCore.QRect(220, 150, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_priority.setFont(font)
        self.lbl_priority.setObjectName(_fromUtf8("lbl_priority"))
        self.lbl_endDate = QtGui.QLabel(Dialog)
        self.lbl_endDate.setGeometry(QtCore.QRect(220, 210, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_endDate.setFont(font)
        self.lbl_endDate.setObjectName(_fromUtf8("lbl_endDate"))
        self.btn_start = QtGui.QPushButton(Dialog)
        self.btn_start.setGeometry(QtCore.QRect(420, 190, 111, 23))
        self.btn_start.setObjectName(_fromUtf8("btn_start"))
        self.btn_end = QtGui.QPushButton(Dialog)
        self.btn_end.setGeometry(QtCore.QRect(420, 220, 111, 23))
        self.btn_end.setObjectName(_fromUtf8("btn_end"))
        self.de_start = QtGui.QDateEdit(Dialog)
        self.de_start.setGeometry(QtCore.QRect(300, 190, 110, 22))
        self.de_start.setObjectName(_fromUtf8("de_start"))
        self.de_end = QtGui.QDateEdit(Dialog)
        self.de_end.setGeometry(QtCore.QRect(300, 220, 110, 22))
        self.de_end.setObjectName(_fromUtf8("de_end"))
        self.lne_task = QtGui.QLineEdit(Dialog)
        self.lne_task.setGeometry(QtCore.QRect(330, 70, 113, 20))
        self.lne_task.setObjectName(_fromUtf8("lne_task"))
        self.lne_assignedby = QtGui.QLineEdit(Dialog)
        self.lne_assignedby.setGeometry(QtCore.QRect(330, 100, 113, 20))
        self.lne_assignedby.setObjectName(_fromUtf8("lne_assignedby"))
        self.lne_duration = QtGui.QLineEdit(Dialog)
        self.lne_duration.setGeometry(QtCore.QRect(330, 130, 113, 20))
        self.lne_duration.setObjectName(_fromUtf8("lne_duration"))
        self.lne_priority = QtGui.QLineEdit(Dialog)
        self.lne_priority.setGeometry(QtCore.QRect(330, 160, 113, 20))
        self.lne_priority.setObjectName(_fromUtf8("lne_priority"))
        self.btn_process = QtGui.QPushButton(Dialog)
        self.btn_process.setGeometry(QtCore.QRect(180, 260, 171, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btn_process.setFont(font)
        self.btn_process.setObjectName(_fromUtf8("btn_process"))
        self.lbl_taskDetails = QtGui.QLabel(Dialog)
        self.lbl_taskDetails.setGeometry(QtCore.QRect(250, 20, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_taskDetails.setFont(font)
        self.lbl_taskDetails.setObjectName(_fromUtf8("lbl_taskDetails"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.btn_process, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Create Tasks", None))
        self.lbl_activities.setText(_translate("Dialog", "Activities", None))
        self.lbl_assignedBy.setText(_translate("Dialog", "Assigned By", None))
        self.lbl_startDate.setText(_translate("Dialog", "Start Date", None))
        self.lbl_taskName.setText(_translate("Dialog", "Task Name", None))
        self.lbl_duration.setText(_translate("Dialog", "Time Duration", None))
        self.lbl_priority.setText(_translate("Dialog", "Priority(1 to 10)", None))
        self.lbl_endDate.setText(_translate("Dialog", "End Date", None))
        self.btn_start.setText(_translate("Dialog", "Select Start Date", None))
        self.btn_end.setText(_translate("Dialog", "Select End Date", None))
        self.btn_process.setText(_translate("Dialog", "Process", None))
        self.lbl_taskDetails.setText(_translate("Dialog", "Enter Task Details", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

