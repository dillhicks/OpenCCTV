# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'models.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui


with open('modelnames.config', 'r') as myfile:
    currentnames = myfile.read()

if currentnames == "":
    currentnames = "None"
global globaltext
globaltext = "Welcome to the model adding tool\nAdd up to 10 well cropped images of faces\n\nCurrent Models:\n" + currentnames + '\n' 
myfile.close()
global filelocation
filelocation = ""
global name
name = ""


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
        MainWindow.resize(351, 449)
        MainWindow.setWindowTitle(_fromUtf8("Model Generator"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 331, 401))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.nameEdit = QtGui.QLineEdit(self.layoutWidget)
        self.nameEdit.setObjectName(_fromUtf8("nameEdit"))
        self.horizontalLayout.addWidget(self.nameEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.openFile = QtGui.QPushButton(self.layoutWidget)
        self.openFile.setObjectName(_fromUtf8("openFile"))
        self.horizontalLayout_2.addWidget(self.openFile)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.addModel = QtGui.QPushButton(self.layoutWidget)
        self.addModel.setObjectName(_fromUtf8("addModel"))
        self.verticalLayout_3.addWidget(self.addModel)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.layoutWidget)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout_3.addWidget(self.plainTextEdit)
        self.pushButton = QtGui.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_3.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.addModel, QtCore.SIGNAL(_fromUtf8("clicked()")), self.addModels)
        QtCore.QObject.connect(self.addModel, QtCore.SIGNAL(_fromUtf8("clicked()")), self.nameEdit.clear)
        QtCore.QObject.connect(self.openFile, QtCore.SIGNAL(_fromUtf8("clicked()")), self.fileDialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.clearModels)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.plainTextEdit.setPlainText(_translate("MainWindow", globaltext, None))
        self.label.setText(_translate("MainWindow", "OpenCCTV: Model Generator", None))
        self.label_2.setText(_translate("MainWindow", "Name:", None))
        self.label_3.setText(_translate("MainWindow", "Choose Image File", None))
        self.openFile.setText(_translate("MainWindow", "Open", None))
        self.addModel.setText(_translate("MainWindow", "Add Model", None))
        self.pushButton.setText(_translate("MainWindow", "Clear Models", None))
        self.nameEdit.setText(_translate("MainWindow", "John Doe", None))
    def fileDialog(self):
        global filelocation
        global globaltext
        filelocation = QtGui.QFileDialog.getOpenFileName(MainWindow, 'Select Image (.jpg)', 'Image files (*.jpg *gif)')
        if filelocation != "":
            globaltext = globaltext + "\n" + filelocation + " set as current image file\n"
            self.plainTextEdit.setPlainText(globaltext)
            self.plainTextEdit.moveCursor(QtGui.QTextCursor.End)
    def clearModels(self):
        open('modellocations.config', 'w').close()
        open('modelnames.config', 'w').close()
        global globaltext
        globaltext = globaltext + "\nModels Cleared\n"
        self.plainTextEdit.setPlainText(globaltext)
        self.plainTextEdit.moveCursor(QtGui.QTextCursor.End)
    def addModels(self):
        name = self.nameEdit.text()
        global fileloaction 
        global globaltext
        with open('modellocations.config', 'a') as file:
            file.write(filelocation + "\n")
            file.close()
        with open('modelnames.config', 'a') as file2:
            file2.write(name + "\n")
            file2.close()
        with open('modelnames.config', 'r') as myfile:
            currentnames = myfile.read()
        globaltext = globaltext + "\n" + name + " added as a Model with location: " + filelocation + "\n\n" + "Current Models:\n" + currentnames + "\n\n"
        self.plainTextEdit.setPlainText(globaltext)
        self.plainTextEdit.moveCursor(QtGui.QTextCursor.End)
        
      





if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

