# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\speed.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *

from speed_config import SpeedConfig
from uart_parse import UARTParser


class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.startPos = None
        self.startPosRelative = None

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        self.startPos = event.globalPos()
        self.startPosRelative = event.pos()
        return super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        if self.startPosRelative != None and self.startPos != None:
            if event.buttons() & Qt.LeftButton:
                movePos = event.globalPos() - self.startPos
                if movePos.manhattanLength() > 4:
                    self.move(event.globalPos() - self.startPosRelative)
        return super().mouseMoveEvent(event)

    def setupUi(self, uart_parser: UARTParser):
        Dialog = self
        Dialog.setObjectName("Dialog")
        Dialog.resize(674, 503)
        self.label = QtWidgets.QLabel(Dialog)

        self.setWindowFlags(Qt.FramelessWindowHint)  # 去边框
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        self.label.setGeometry(QtCore.QRect(50, 0, 591, 471))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(".\\Assests/background.webp"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(290, 330, 131, 51))
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "    color:White;\n"
                                      "    border-radius: 7px;\n"
                                      "    font-family:微软雅黑;\n"
                                      "    background:#6633FF;\n"
                                      "    border:1px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "    background:#6666FF;\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "    background:#6600FF;\n"
                                      "}")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 60, 31, 31))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "    background:#CE0000;\n"
                                        "    color:white;\n"
                                        "    font-size:18px;\n"
                                        "    border-radius: 12px;\n"
                                        "    font-family: Consolas;\n"
                                        "}\n"
                                        "QPushButton:hover{                    \n"
                                        "    background:#FF2D2D;\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    border: 1px solid #3C3C3C!important;\n"
                                        "    background:#AE0000;\n"
                                        "}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(110, 60, 41, 41))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(".\\Assests/icon.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(200, 160, 101, 31))
        self.label_2.setStyleSheet("QLabel{\n"
                                   "    background:#6C6C6C;\n"
                                   "    color:white;\n"
                                   "    font-size:16px;\n"
                                   "    border-radius:\n"
                                   "    8px;font-family: 微软雅黑;\n"
                                   "}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalSlider = QtWidgets.QSlider(Dialog)
        self.horizontalSlider.setGeometry(QtCore.QRect(330, 160, 101, 31))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(200, 220, 101, 31))
        self.label_3.setStyleSheet("QLabel{\n"
                                   "    background:#6C6C6C;\n"
                                   "    color:white;\n"
                                   "    font-size:16px;\n"
                                   "    border-radius:\n"
                                   "    8px;font-family: 微软雅黑;\n"
                                   "}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(330, 220, 101, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(440, 220, 71, 31))
        self.comboBox_3.setStyleSheet("QComboBox{\n"
                                      "    font-size:18px;\n"
                                      "    font-family: Consolas;\n"
                                      "}")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(440, 160, 71, 31))
        self.label_8.setStyleSheet("QLabel{\n"
                                   "    background:#FFFFFF;\n"
                                   "    color:black;\n"
                                   "    font-size:24px;\n"
                                   "    border-radius:\n"
                                   "    8px;font-family: Consolas;\n"
                                   "}")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")

        self.comboBox_6 = QtWidgets.QComboBox(Dialog)
        self.comboBox_6.setGeometry(QtCore.QRect(330, 280, 101, 31))
        self.comboBox_6.setStyleSheet("QComboBox{\n"
                                      "    font-size:18px;\n"
                                      "    font-family: Consolas;\n"
                                      "}")
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")

        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(200, 280, 101, 31))
        self.label_12.setStyleSheet("QLabel{\n"
                                    "    background:#6C6C6C;\n"
                                    "    color:white;\n"
                                    "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);\n"
                                    "    font-size:16px;\n"
                                    "    border-radius:\n"
                                    "    8px;font-family: 微软雅黑;\n"
                                    "}")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton_3.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.apply_changes)
        self.horizontalSlider.valueChanged.connect(self.update_speed_preview)

        self.speed_config = SpeedConfig(uart_parser)

    def apply_changes(self):
        self.speed_config.speed = self.horizontalSlider.value()
        self.speed_config.mode = self.comboBox_6.currentIndex()
        if self.lineEdit.text() != "":
            self.speed_config.count_down = int(self.lineEdit.text())
        else:
            self.speed_config.count_down = 0
        if self.comboBox_3.currentData() == "分钟":
            self.speed_config.count_down *= 60
        elif self.comboBox_3.currentData() == "小时":
            self.speed_config.count_down *= 3600
        self.speed_config.send()
        self.close()

    def update_speed_preview(self):
        _translate = QtCore.QCoreApplication.translate
        speed = self.horizontalSlider.value()
        self.label_8.setText(_translate("Form", f"{speed}%"))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "应用"))
        self.pushButton_3.setText(_translate("Dialog", "X"))
        self.label_2.setText(_translate("Dialog", "转速"))
        self.label_3.setText(_translate("Dialog", "定时"))

        self.comboBox_3.setItemText(0, _translate("Dialog", "秒"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "分钟"))
        self.comboBox_3.setItemText(2, _translate("Dialog", "小时"))

        self.comboBox_6.setItemText(0, _translate("Dialog", "手动"))
        self.comboBox_6.setItemText(1, _translate("Dialog", "自动"))
        self.comboBox_6.setItemText(2, _translate("Dialog", "自然风"))

        self.label_12.setText(_translate("Dialog", "运行模式"))
        self.label_8.setText(_translate("Dialog", "%"))
