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
        self.OpenFansButton.setGeometry(QtCore.QRect(350, 340, 171, 41))
        self.OpenFansButton.setObjectName("OpenFansButton")
        self.CloseFansButton = QtWidgets.QPushButton(Form)
        self.CloseFansButton.setGeometry(QtCore.QRect(540, 340, 171, 41))
        self.CloseFansButton.setObjectName("CloseFansButton")
        self.Year = QtWidgets.QTextBrowser(Form)
        self.Year.setGeometry(QtCore.QRect(310, 40, 171, 121))
        self.Year.setObjectName("Year")
        self.Time = QtWidgets.QTextBrowser(Form)
        self.Time.setGeometry(QtCore.QRect(520, 40, 171, 121))
        self.Time.setObjectName("Time")
        self.Status = QtWidgets.QTextBrowser(Form)
        self.Status.setGeometry(QtCore.QRect(310, 170, 171, 61))
        self.Status.setObjectName("Status")

        self.retranslateUi(Form)
        self.OpenFansButton.clicked.connect(Form.OpenFans)
        self.CloseFansButton.clicked.connect(Form.CloseFans)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.OpenFansButton.setText(_translate("Form", "Open"))
        self.CloseFansButton.setText(_translate("Form", "Close"))
        self.Status.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">状态：</span></p></body></html>"))

