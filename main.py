#coding:utf-8
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os
import time
#import paho.mqtt
from MyAgent import Ui_Form


class mywindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("RaspberryPI")
        self.use_palette()
        #self.setWindowTitle("mywindow")
        #self.setWindowIcon(QIcon("title.ico"))
        #self.Year.setText(year.toString())
        #self.Time.setText(time.toString())
        self.Year.setText(time.strftime("%x", time.localtime()))
        #self.Year.setCurrentFont(QFont("Microsoft YaHei", 8, QFont::Normal))
        self.Time.setText(time.strftime("%X", time.localtime()))

        self.year = QTimer()
        self.year.setInterval(1000)
        self.year.start()

        self.timer = QTimer()
        self.timer.setInterval(1000)       
        self.timer.start()
        # 信号连接到槽
        self.year.timeout.connect(lambda:self.onDateOut())
        self.timer.timeout.connect(lambda:self.onTimerOut())
        self.OpenFansButton.setToolTip("This is a <b>QPushButon</b> widget")

    def onTimerOut(self):        
        self.Time.setText(time.strftime("%X",time.localtime()))

    def onDateOut(self):
        self.Year.setText(time.strftime("%x",time.localtime()))

    def OpenFans(self):
        self.Status.setText("状态：打开")
        os.popen('mosquitto_pub -t gpio -h 1.1.1.1 -m "{\\"pin\\":17,\\"value\\":1}"')

    def CloseFans(self):
        self.Status.setText("状态：关闭")
        #os.popen函数不接收单个的'\'，因此需要'\\'转义
        os.popen('mosquitto_pub -t gpio -h 1.1.1.1 -m "{\\"pin\\":17,\\"value\\":0}"')

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

#    def paintEvent(self, QPaintEvent):
#        palette1 = QtGui.QPalette(self)
#        #palette1.setColor(self.backgroundRole(), QColor(192, 253, 123))  # 设置背景颜色
#        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("background.jpg")))  # 设置背景图片
#        #painter.drawPixmap(0, 0, 256, 256, QPixmap("1.png"))
#        self.setPalette(palette1)

    def use_palette(self):
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(),
        QtGui.QBrush(QtGui.QPixmap("background.jpg")))
        self.setPalette(window_pale)

if __name__==  '__main__':
    app = QtWidgets.QApplication(sys.argv)
 #   year = QDate.currentDate()
 #   time = QTime.currentTime()

    window = mywindow()
    window.show()
    sys.exit(app.exec_())
