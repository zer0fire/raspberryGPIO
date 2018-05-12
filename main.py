#coding:utf-8
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
import sys
import os
#import paho.mqtt

from MyAgent import Ui_Form

class mywindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("RaspberryPI")
        #self.setWindowTitle("mywindow")
        #self.setWindowIcon(QIcon("title.ico"))
        self.OpenFansButton.setToolTip("This is a <b>QPushButon</b> widget")

    def OpenFans(self):
        self.Status.setText("状态：打开")
        os.popen('mosquitto_pub -t gpio -h 1.1.1.1 -m "{\"pin\":17,\"value\":1}"')

    def CloseFans(self):
        self.Status.setText("状态：关闭")
        os.popen('mosquitto_pub -t gpio -h 1.1.1.1 -m "{\"pin\":17,\"value\":0}"')

    def DashBoardPage(self):
        pass

    def ControlButtonPage(self):
        pass

    def AdditionPage(self):
        pass

    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self, "关闭提示", "真的要退出吗？", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

if __name__==  '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())
