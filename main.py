#coding:utf-8
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
import sys

from MyAgent import Ui_Form

class mywindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("RaspberryPI")
        #self.setWindowTitle("mywindow")
        #self.setWindowIcon(QIcon("title.ico"))
        self.helloButton.setToolTip("This is a <b>QPushButon</b> widget")

    def OpenFans(self):
        pass

    def CloseFans(self):
        pass

    def DashBoardPage(self):
        pass

    def ControlButtonPage(self):
        pass

    def AdditionPage(self):
        pass

if __name__==  '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())