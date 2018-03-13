from PyQt4 import QtCore, QtGui
import mot as md
import fac as m  

global globaloutput

globaloutput = "------------------------------\nWelcome to the Smart Security Camera!\nSet your email below to send email alerts!\nSet your phone number below to send text alerts!\nStart recording with the buttons below!\n------------------------------"
with open('main.config', 'r') as file:
    data = file.readlines()
file.close    
data[0] = 'false\n'
data[1] = 'false\n'

with open('main.config', 'w') as file:
    file.writelines(data)
file.close




globaloutput = globaloutput + "\nCurrent Email: " + data[2] + "Current Phone: " + data[3] + "\n"

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
        MainWindow.resize(559, 595)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 510, 68, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(90, 510, 171, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 540, 68, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(90, 540, 141, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 9, 541, 338))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.emailCheck = QtGui.QCheckBox(self.layoutWidget)
        self.emailCheck.setObjectName(_fromUtf8("emailCheck"))
        self.horizontalLayout.addWidget(self.emailCheck)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.textCheck = QtGui.QCheckBox(self.layoutWidget)
        self.textCheck.setObjectName(_fromUtf8("textCheck"))
        self.horizontalLayout_2.addWidget(self.textCheck)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.layoutWidget)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.facialButton = QtGui.QPushButton(self.layoutWidget)
        self.facialButton.setObjectName(_fromUtf8("facialButton"))
        self.horizontalLayout_4.addWidget(self.facialButton)
        self.motionButton = QtGui.QPushButton(self.layoutWidget)
        self.motionButton.setObjectName(_fromUtf8("motionButton"))
        self.horizontalLayout_4.addWidget(self.motionButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.standardButton = QtGui.QPushButton(self.layoutWidget)
        self.standardButton.setObjectName(_fromUtf8("standardButton"))
        self.verticalLayout_2.addWidget(self.standardButton)
        self.gridLayout.addLayout(self.verticalLayout_2, 3, 0, 1, 1)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 330, 541, 162))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_5 = QtGui.QLabel(self.layoutWidget1)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lineEdit = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_5.addWidget(self.lineEdit)
        self.pushButton = QtGui.QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_6 = QtGui.QLabel(self.layoutWidget1)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_6.addWidget(self.label_6)
        self.lineEdit_2 = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_6.addWidget(self.lineEdit_2)
        self.pushButton_2 = QtGui.QPushButton(self.layoutWidget1)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_6.addWidget(self.pushButton_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setCheckable(True)
        self.actionClose.setChecked(True)
        self.actionClose.setIconVisibleInMenu(True)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.emailCheck, QtCore.SIGNAL(_fromUtf8("clicked()")), self.emailBox)
        QtCore.QObject.connect(self.textCheck, QtCore.SIGNAL(_fromUtf8("clicked()")), self.phoneBox)
        QtCore.QObject.connect(self.motionButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.motionStart)
        QtCore.QObject.connect(self.facialButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.facialStart)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.setEmail)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit.clear) #lineEdit = email edit
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.setPhone)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_2.clear) #lineEdit2 = phone edit
    
    def emailBox(self):
        global globaloutput
        status = self.emailCheck.isChecked()
        if(status):
            globaloutput = globaloutput + "\nUsing email"
            self.plainTextEdit.setPlainText(globaloutput)
            self.plainTextEdit.moveCursor(QtGui.QTextCursor.End)
            with open('main.config','r') as file:
                data = file.readlines()
            file.close()
            data[0] = str("true" + '\n')
            with open('main.config', 'w') as file:
                file.writelines(data)
            file.close()

        elif(status == False):
            globaloutput = globaloutput + "\nNot using email"
            self.plainTextEdit.setPlainText(globaloutput)
            self.plainTextEdit.moveCursor(QtGui.QTextCursor.End)
            with open('main.config','r') as file:
                data = file.readlines()
            file.close()
            data[0] = str("false" + '\n')
            with open('main.config', 'w') as file:
                file.writelines(data)
            file.close()

    def phoneBox(self):     
        global globaloutput
        if self.textCheck.isChecked():
            globaloutput = globaloutput + "\nUsing text"
            self.plainTextEdit.setPlainText(globaloutput)
            self.plainTextEdit.moveCursor(QtGui.QTextCursor.End)
            with open('main.config','r') as file:
                data = file.readlines()
            file.close()
            data[1] = str("true" + '\n')
            with open('main.config', 'w') as file:
                file.writelines(data)
            file.close()
        else:
            globaloutput = globaloutput + "\nNot using email"
            self.plainTextEdit.setPlainText(globaloutput)
            self.plainTextEdit.moveCursor(QtGui.QTextCursor.End)
            with open('main.config','r') as file:
                data = file.readlines()
            file.close()
            data[1] = str("false" + '\n')
            with open('main.config', 'w') as file:
                file.writelines(data)
            file.close()

    def motionStart(self):
        global globaloutput
        globaloutput = globaloutput + "\n------------------------------\nStarted Motion Detection\n------------------------------"
        self.plainTextEdit.setPlainText(globaloutput)
        self.plainTextEdit.moveCursor(QtGui.QTextCursor.End)
        try:
            md.motionStart()
        except:
            globaloutput = globaloutput + "\n------------------------------\nOut of Memory Please Restart Program!\n------------------------------"
            self.plainTextEdit.setPlainText(globaloutput)
            self.plainTextEdit.moveCursor(QtGui.QTextCursor.End)

    def facialStart(self):
        global globaloutput
        globaloutput = globaloutput + "\n------------------------------\nStarted Facial Recognition\n------------------------------"
        self.plainTextEdit.setPlainText(globaloutput)
        self.plainTextEdit.moveCursor(QtGui.QTextCursor.End)
        try:
            m.facialStart()
        except:
            globaloutput = globaloutput + "\n------------------------------\nOut of Memory Please Restart Program!\n------------------------------"
            self.plainTextEdit.setPlainText(globaloutput)
            self.plainTextEdit.moveCursor(QtGui.QTextCursor.End)

     
    def setEmail(self):
        #label_10 = emailtext
        global globaloutput
        output = "\nEmail added as: "
        self.label_10.setText(self.lineEdit.text())
        currentemail = self.lineEdit.text()
        globaloutput = globaloutput + output + currentemail
        self.plainTextEdit.setPlainText(globaloutput)
        self.plainTextEdit.moveCursor(QtGui.QTextCursor.End)
        with open('main.config','r') as file:
            data = file.readlines()
        file.close()
        data[2] = str(currentemail + '\n')
        with open('main.config', 'w') as file:
            file.writelines(data)
        file.close()

    def setPhone(self):
        global globaloutput
        text = "\nPhone added as: "
        self.label_8.setText(self.lineEdit_2.text())
        currentphone = self.lineEdit_2.text()
        globaloutput = globaloutput + text + currentphone
        self.plainTextEdit.setPlainText(globaloutput)
        self.plainTextEdit.moveCursor(QtGui.QTextCursor.End)
        with open('main.config','r') as file:
            data = file.readlines()
        file.close()
        data[3] = str(currentphone + '\n')
        with open('main.config', 'w') as file:
            file.writelines(data) 
        #label_8 = phonetext


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Security Camera", None))
        self.label_7.setText(_translate("MainWindow", "Phone:", None))
        self.label_8.setText(_translate("MainWindow", "Enter Phone Number", None))
        self.label_9.setText(_translate("MainWindow", "Email: ", None))
        self.label_10.setText(_translate("MainWindow", "Enter Email", None))
        self.label_3.setText(_translate("MainWindow", "Use Email?", None))
        self.emailCheck.setText(_translate("MainWindow", "Yes", None))
        self.label_4.setText(_translate("MainWindow", "Use Text?", None))
        self.textCheck.setText(_translate("MainWindow", "Yes", None))
        self.plainTextEdit.setPlainText(_translate("MainWindow",globaloutput , None))
        self.facialButton.setText(_translate("MainWindow", "Facial Detection", None))
        self.motionButton.setText(_translate("MainWindow", "Motion Detection", None))
        self.standardButton.setText(_translate("MainWindow", "Standard Record (Dumb Recording)", None))
        self.label.setText(_translate("MainWindow", "Click to start recording!", None))
        self.label_2.setText(_translate("MainWindow", "OpenCCTV : Smart Security Camera", None))
        self.label_5.setText(_translate("MainWindow", "Email:", None))
        self.lineEdit.setText(_translate("MainWindow", "example@email.com", None))
        self.pushButton.setText(_translate("MainWindow", "Set", None))
        self.label_6.setText(_translate("MainWindow", "Phone:", None))
        self.lineEdit_2.setText(_translate("MainWindow", "+12345678910", None))
        self.pushButton_2.setText(_translate("MainWindow", "Set", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
    

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

