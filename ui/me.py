# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'me.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1009, 757)
        Dialog.setStyleSheet("#Dialog{background-image: url(:/back1.png)}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, -20, 861, 231))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton1 = QtWidgets.QPushButton(Dialog)
        self.pushButton1.setGeometry(QtCore.QRect(400, 250, 221, 71))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton1.setFont(font)
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton2 = QtWidgets.QPushButton(Dialog)
        self.pushButton2.setGeometry(QtCore.QRect(400, 340, 221, 71))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton2.setFont(font)
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton3 = QtWidgets.QPushButton(Dialog)
        self.pushButton3.setGeometry(QtCore.QRect(400, 430, 221, 71))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton3.setFont(font)
        self.pushButton3.setObjectName("pushButton3")
        self.pushButton4 = QtWidgets.QPushButton(Dialog)
        self.pushButton4.setGeometry(QtCore.QRect(400, 520, 221, 71))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton4.setFont(font)
        self.pushButton4.setObjectName("pushButton4")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 40, 861, 231))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        self.pushButton1.clicked.connect(Dialog.goin1) # type: ignore
        self.pushButton2.clicked.connect(Dialog.goin2) # type: ignore
        self.pushButton3.clicked.connect(Dialog.goin3) # type: ignore
        self.pushButton4.clicked.connect(Dialog.goin4) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "停车场车辆进出智能监控系统"))
        self.pushButton1.setText(_translate("Dialog", "查看入口A监控画面"))
        self.pushButton2.setText(_translate("Dialog", "查看出口A监控画面"))
        self.pushButton3.setText(_translate("Dialog", "查看车辆入场记录"))
        self.pushButton4.setText(_translate("Dialog", "查看车辆出场记录"))
        self.label_2.setText(_translate("Dialog", "欢迎您"))
import data.background_image_rc
