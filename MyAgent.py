# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyAgent.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(812, 431)
        self.OpenFansButton = QtWidgets.QPushButton(Form)
        self.OpenFansButton.setGeometry(QtCore.QRect(350, 290, 171, 41))
        self.OpenFansButton.setObjectName("OpenFansButton")
        self.CloseFansButton = QtWidgets.QPushButton(Form)
        self.CloseFansButton.setGeometry(QtCore.QRect(540, 290, 171, 41))
        self.CloseFansButton.setObjectName("CloseFansButton")
        self.Year = QtWidgets.QTextBrowser(Form)
        self.Year.setGeometry(QtCore.QRect(350, 90, 171, 121))
        self.Year.setObjectName("Year")
        self.Time = QtWidgets.QTextBrowser(Form)
        self.Time.setGeometry(QtCore.QRect(540, 90, 171, 121))
        self.Time.setObjectName("Time")
        self.Page1Button = QtWidgets.QPushButton(Form)
        self.Page1Button.setGeometry(QtCore.QRect(0, 40, 121, 31))
        self.Page1Button.setObjectName("Page1Button")
        self.Page2Button = QtWidgets.QPushButton(Form)
        self.Page2Button.setGeometry(QtCore.QRect(0, 70, 121, 31))
        self.Page2Button.setObjectName("Page2Button")
        self.Page3Button = QtWidgets.QPushButton(Form)
        self.Page3Button.setGeometry(QtCore.QRect(0, 100, 121, 31))
        self.Page3Button.setObjectName("Page3Button")

        self.retranslateUi(Form)
        self.OpenFansButton.clicked.connect(Form.OpenFans)
        self.CloseFansButton.clicked.connect(Form.CloseFans)
        self.Page1Button.clicked.connect(Form.DashBoardPage)
        self.Page2Button.clicked.connect(Form.ControlButtonPage)
        self.Page3Button.clicked.connect(Form.AdditionPage)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.OpenFansButton.setText(_translate("Form", "Open"))
        self.CloseFansButton.setText(_translate("Form", "Close"))
        self.Page1Button.setText(_translate("Form", "仪表"))
        self.Page2Button.setText(_translate("Form", "按键"))
        self.Page3Button.setText(_translate("Form", "附加项"))

