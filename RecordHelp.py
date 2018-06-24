# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'help.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QResource
import sys
import resource

class RecordHelp(QWidget):
  
    def __init__(self, parent = None):
        super(RecordHelp, self).__init__(parent) 
        self.setupUi()
        
    def setupUi(self):
        self.setObjectName("Form")
        self.setFixedSize(600, 310)
        # QResource.registerResource('C:\Users\lv\ctest\record-camera-and-screen\test.qrc', 'resource')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resource/gutin.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(60, 330, 229, 10))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(40, 30, 181, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/resource/gutin.jpg"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(250, 30, 281, 31))
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.status_title = QtWidgets.QLabel(self)
        self.status_title.setGeometry(QtCore.QRect(250, 60, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.status_title.setFont(font)
        self.status_title.setScaledContents(True)
        self.status_title.setWordWrap(True)
        self.status_title.setObjectName("status_title")
        self.start = QtWidgets.QLabel(self)
        self.start.setGeometry(QtCore.QRect(290, 130, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.start.setFont(font)
        self.start.setText("")
        self.start.setPixmap(QtGui.QPixmap(":/resource/start.png"))
        self.start.setScaledContents(True)
        self.start.setObjectName("start")
        self.camera = QtWidgets.QLabel(self)
        self.camera.setGeometry(QtCore.QRect(380, 130, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.camera.setFont(font)
        self.camera.setText("")
        self.camera.setPixmap(QtGui.QPixmap(":/resource/camera_recording_colorful.png"))
        self.camera.setScaledContents(True)
        self.camera.setObjectName("camera")
        self.screen = QtWidgets.QLabel(self)
        self.screen.setGeometry(QtCore.QRect(470, 130, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.screen.setFont(font)
        self.screen.setText("")
        self.screen.setPixmap(QtGui.QPixmap(":/resource/screen_recording.png"))
        self.screen.setScaledContents(True)
        self.screen.setObjectName("screen")
        self.start_label = QtWidgets.QLabel(self)
        self.start_label.setGeometry(QtCore.QRect(290, 200, 61, 16))
        self.start_label.setObjectName("start_label")
        self.camera_label = QtWidgets.QLabel(self)
        self.camera_label.setGeometry(QtCore.QRect(380, 200, 61, 16))
        self.camera_label.setObjectName("camera_label")
        self.start_label_2 = QtWidgets.QLabel(self)
        self.start_label_2.setGeometry(QtCore.QRect(480, 200, 51, 16))
        self.start_label_2.setObjectName("start_label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(40, 240, 541, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.frame.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.status_title.raise_()
        self.start.raise_()
        self.camera.raise_()
        self.screen.raise_()
        self.start_label.raise_()
        self.camera_label.raise_()
        self.start_label_2.raise_()
        self.label_3.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "帮助"))
        self.label_2.setText(_translate("Form", "<h2>谷田会议视频录播管理系统-帮助</h2>"))
        self.label_2.setStyleSheet('color:blue')
        self.status_title.setText(_translate("Form", "1.软件主要功能是录制摄像头和录制屏幕，有非录制状态、录制摄像头、录制屏幕三种状态主要以托盘图标的变化来区分："))
        self.status_title.setStyleSheet('font-weight:bold')
        self.start_label.setText(_translate("Form", "非录制状态"))
        self.camera_label.setText(_translate("Form", "录制摄像头"))
        self.start_label_2.setText(_translate("Form", "录制屏幕"))
        self.label_3.setText(_translate("Form", "2.此软件需配合谷田智能会议硬件使用，已申请国家专利，未经事先书面许可，严禁进行任何形式的仿制、改装并用于销售、复制、改编或翻译，除非版权法另有规定。"))
        self.label_3.setStyleSheet('font-weight:bold')

     
    def showWindow(self):
        if not self.isVisible():
            self.show()
            
    def closeEvent(self, event):
        # self.setVisible(False)
        # event.ignore()
        pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    rh = RecordHelp()
    rh.show()  
    sys.exit(app.exec_()) 