# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tasks.ui'
#
# Created: Fri Mar 22 13:03:06 2019
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
        Dialog.resize(628, 339)
        self.btn_add = QtGui.QPushButton(Dialog)
        self.btn_add.setGeometry(QtCore.QRect(150, 290, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_add.setFont(font)
        self.btn_add.setObjectName(_fromUtf8("btn_add"))
        self.tableView = QtGui.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(10, 80, 591, 192))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.btn_save = QtGui.QPushButton(Dialog)
        self.btn_save.setGeometry(QtCore.QRect(350, 290, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_save.setFont(font)
        self.btn_save.setObjectName(_fromUtf8("btn_save"))
        self.lbl_filter = QtGui.QLabel(Dialog)
        self.lbl_filter.setGeometry(QtCore.QRect(10, 50, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_filter.setFont(font)
        self.lbl_filter.setObjectName(_fromUtf8("lbl_filter"))
        self.cb_options = QtGui.QComboBox(Dialog)
        self.cb_options.setGeometry(QtCore.QRect(70, 50, 91, 22))
        self.cb_options.setObjectName(_fromUtf8("cb_options"))
        self.cb_options.addItem(_fromUtf8(""))
        self.cb_options.addItem(_fromUtf8(""))
        self.cb_options.addItem(_fromUtf8(""))
        self.cb_options.addItem(_fromUtf8(""))
        self.cb_options.addItem(_fromUtf8(""))
        self.cb_options.addItem(_fromUtf8(""))
        self.cb_options.addItem(_fromUtf8(""))
        self.cb_options.addItem(_fromUtf8(""))
        self.cb_options.addItem(_fromUtf8(""))
        self.lbl_tasks = QtGui.QLabel(Dialog)
        self.lbl_tasks.setGeometry(QtCore.QRect(290, 10, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_tasks.setFont(font)
        self.lbl_tasks.setObjectName(_fromUtf8("lbl_tasks"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(170, 50, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lbl_sort = QtGui.QLabel(Dialog)
        self.lbl_sort.setGeometry(QtCore.QRect(320, 50, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_sort.setFont(font)
        self.lbl_sort.setObjectName(_fromUtf8("lbl_sort"))
        self.cb_sort = QtGui.QComboBox(Dialog)
        self.cb_sort.setGeometry(QtCore.QRect(380, 50, 91, 22))
        self.cb_sort.setObjectName(_fromUtf8("cb_sort"))
        self.cb_sort.addItem(_fromUtf8(""))
        self.cb_sort.addItem(_fromUtf8(""))
        self.cb_sort.addItem(_fromUtf8(""))
        self.cb_sort.addItem(_fromUtf8(""))
        self.btn_filtersort = QtGui.QPushButton(Dialog)
        self.btn_filtersort.setGeometry(QtCore.QRect(490, 50, 121, 23))
        self.btn_filtersort.setObjectName(_fromUtf8("btn_filtersort"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.btn_add.setText(_translate("Dialog", "Add Task", None))
        self.btn_save.setText(_translate("Dialog", "Save Changes", None))
        self.lbl_filter.setText(_translate("Dialog", " Filter by :", None))
        self.cb_options.setItemText(0, _translate("Dialog", "Options", None))
        self.cb_options.setItemText(1, _translate("Dialog", "Activity name", None))
        self.cb_options.setItemText(2, _translate("Dialog", "Activity type", None))
        self.cb_options.setItemText(3, _translate("Dialog", "Assigned by", None))
        self.cb_options.setItemText(4, _translate("Dialog", "Task name", None))
        self.cb_options.setItemText(5, _translate("Dialog", "Start date", None))
        self.cb_options.setItemText(6, _translate("Dialog", "End date", None))
        self.cb_options.setItemText(7, _translate("Dialog", "Status", None))
        self.cb_options.setItemText(8, _translate("Dialog", "Priority", None))
        self.lbl_tasks.setText(_translate("Dialog", "Tasks", None))
        self.lbl_sort.setText(_translate("Dialog", "Sort by :", None))
        self.cb_sort.setItemText(0, _translate("Dialog", "Options", None))
        self.cb_sort.setItemText(1, _translate("Dialog", "Start date", None))
        self.cb_sort.setItemText(2, _translate("Dialog", "End date", None))
        self.cb_sort.setItemText(3, _translate("Dialog", "Priority", None))
        self.btn_filtersort.setText(_translate("Dialog", "Sort and Filter", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

