# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controller.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import servo as sc
import time
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        Form.setMinimumSize(QtCore.QSize(400, 300))
        Form.setMaximumSize(QtCore.QSize(400, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../Desktop/3901.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 20, 351, 241))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.upButton = QtGui.QPushButton(self.widget)
        self.upButton.setObjectName(_fromUtf8("upButton"))
        self.gridLayout.addWidget(self.upButton, 0, 1, 1, 1)
        self.leftButton = QtGui.QPushButton(self.widget)
        self.leftButton.setObjectName(_fromUtf8("leftButton"))
        self.gridLayout.addWidget(self.leftButton, 1, 0, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.widget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 1, 1, 1, 1)
        self.rightButton = QtGui.QPushButton(self.widget)
        self.rightButton.setObjectName(_fromUtf8("rightButton"))
        self.gridLayout.addWidget(self.rightButton, 1, 2, 1, 1)
        self.downButton = QtGui.QPushButton(self.widget)
        self.downButton.setObjectName(_fromUtf8("downButton"))
        self.gridLayout.addWidget(self.downButton, 2, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.rightButton, QtCore.SIGNAL(_fromUtf8("clicked()")), sc.moveRight)
        QtCore.QObject.connect(self.upButton, QtCore.SIGNAL(_fromUtf8("clicked()")), sc.moveUp)
        QtCore.QObject.connect(self.leftButton, QtCore.SIGNAL(_fromUtf8("clicked()")), sc.moveLeft)
        QtCore.QObject.connect(self.downButton, QtCore.SIGNAL(_fromUtf8("clicked()")), sc.moveDown)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), sc.center)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Camera Controller", None))
        self.upButton.setText(_translate("Form", "⇑", None))
        self.leftButton.setText(_translate("Form", "⇐", None))
        self.pushButton_3.setText(_translate("Form", "Center", None))
        self.rightButton.setText(_translate("Form", "⇒", None))
        self.downButton.setText(_translate("Form", "⇓", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

