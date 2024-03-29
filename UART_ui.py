# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UART.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from uart_parse import UARTParser, get_uart_default_settings, get_uart_port_list


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
        Dialog.resize(657, 511)

        self.setWindowFlags(Qt.FramelessWindowHint)  # 去边框
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, -20, 601, 531))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(".\\Assests/background.webp"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(330, 370, 131, 51))
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
        self.pushButton_3.setGeometry(QtCore.QRect(520, 50, 31, 31))
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
        self.label_7.setGeometry(QtCore.QRect(80, 50, 41, 41))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(".\\Assests/icon.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(210, 140, 101, 31))
        self.label_8.setStyleSheet("QLabel{\n"
                                   "    background:#6C6C6C;\n"
                                   "    color:white;\n"
                                   "    font-size:16px;\n"
                                   "    border-radius:\n"
                                   "    8px;font-family: 微软雅黑;\n"
                                   "}")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(210, 180, 101, 31))
        self.label_9.setStyleSheet("QLabel{\n"
                                   "    background:#6C6C6C;\n"
                                   "    color:white;\n"
                                   "    font-size:16px;\n"
                                   "    border-radius:\n"
                                   "    8px;font-family: 微软雅黑;\n"
                                   "}")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(210, 220, 101, 31))
        self.label_10.setStyleSheet("QLabel{\n"
                                    "    background:#6C6C6C;\n"
                                    "    color:white;\n"
                                    "    font-size:16px;\n"
                                    "    border-radius:\n"
                                    "    8px;font-family: 微软雅黑;\n"
                                    "}")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(210, 260, 101, 31))
        self.label_11.setStyleSheet("QLabel{\n"
                                    "    background:#6C6C6C;\n"
                                    "    color:white;\n"
                                    "    font-size:16px;\n"
                                    "    border-radius:\n"
                                    "    8px;font-family: 微软雅黑;\n"
                                    "}")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(210, 300, 101, 31))
        self.label_12.setStyleSheet("QLabel{\n"
                                    "    background:#6C6C6C;\n"
                                    "    color:white;\n"
                                    "    font-size:16px;\n"
                                    "    border-radius:\n"
                                    "    8px;font-family: 微软雅黑;\n"
                                    "}")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(330, 180, 101, 31))
        self.comboBox_3.setStyleSheet("QComboBox{\n"
                                      "    font-size:18px;\n"
                                      "    font-family: Consolas;\n"
                                      "}")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(Dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(330, 220, 101, 31))
        self.comboBox_4.setStyleSheet("QComboBox{\n"
                                      "    font-size:18px;\n"
                                      "    font-family: Consolas;\n"
                                      "}")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_5 = QtWidgets.QComboBox(Dialog)
        self.comboBox_5.setGeometry(QtCore.QRect(330, 260, 101, 31))
        self.comboBox_5.setStyleSheet("QComboBox{\n"
                                      "    font-size:18px;\n"
                                      "    font-family: Consolas;\n"
                                      "}")
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_6 = QtWidgets.QComboBox(Dialog)
        self.comboBox_6.setGeometry(QtCore.QRect(330, 300, 101, 31))
        self.comboBox_6.setStyleSheet("QComboBox{\n"
                                      "    font-size:18px;\n"
                                      "    font-family: Consolas;\n"
                                      "}")
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 370, 131, 51))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
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
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(330, 140, 101, 31))
        self.comboBox_2.setStyleSheet("QComboBox{\n"
                                      "    font-size:18px;\n"
                                      "    font-family: Consolas;\n"
                                      "}")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.uart_parser = uart_parser

        self.update_available_ports()

        self.update_settings_preview()

        self.pushButton_3.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.set_to_default)
        self.pushButton.clicked.connect(self.apply_changes)

    def update_available_ports(self):
        _translate = QtCore.QCoreApplication.translate
        available_ports = get_uart_port_list()
        self.comboBox_2.clear()
        for index, port in enumerate(available_ports):
            self.comboBox_2.addItem("")
            self.comboBox_2.setItemText(index, _translate("Dialog", port))

    def update_settings_preview(self):
        inv_parity_table = {'N': "无校验", 'E': "奇校验", 'O': "偶校验"}
        self.comboBox_2.setCurrentIndex(
            self.comboBox_2.findText(self.uart_parser.port))
        self.comboBox_3.setCurrentIndex(
            self.comboBox_3.findText(str(self.uart_parser.baudrate)))
        self.comboBox_4.setCurrentIndex(
            self.comboBox_4.findText(str(self.uart_parser.bytesize)))
        self.comboBox_6.setCurrentIndex(
            self.comboBox_6.findText(inv_parity_table[self.uart_parser.parity]))
        self.comboBox_5.setCurrentIndex(
            self.comboBox_5.findText(str(self.uart_parser.stopbits)))

    def set_to_default(self):
        self.uart_parser.set_to_default()
        self.update_settings_preview()

    def apply_changes(self):
        parity_table = {"无校验": 'N', "奇校验": 'E', "偶校验": 'O'}
        self.uart_parser.port = self.comboBox_2.currentText()
        self.uart_parser.baudrate = int(self.comboBox_3.currentText())
        self.uart_parser.bytesize = int(self.comboBox_4.currentText())
        self.uart_parser.parity = parity_table[self.comboBox_6.currentText()]
        self.uart_parser.stopbits = int(self.comboBox_5.currentText())
        self.uart_parser.reconnect()
        self.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "应用"))
        self.pushButton_3.setText(_translate("Dialog", "X"))
        self.label_8.setText(_translate("Dialog", "端口"))
        self.label_9.setText(_translate("Dialog", "波特率"))
        self.label_10.setText(_translate("Dialog", "数据位"))
        self.label_11.setText(_translate("Dialog", "停止位"))
        self.label_12.setText(_translate("Dialog", "校验位"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "50"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "75"))
        self.comboBox_3.setItemText(2, _translate("Dialog", "110"))
        self.comboBox_3.setItemText(3, _translate("Dialog", "134"))
        self.comboBox_3.setItemText(4, _translate("Dialog", "150"))
        self.comboBox_3.setItemText(5, _translate("Dialog", "200"))
        self.comboBox_3.setItemText(6, _translate("Dialog", "300"))
        self.comboBox_3.setItemText(7, _translate("Dialog", "600"))
        self.comboBox_3.setItemText(8, _translate("Dialog", "1200"))
        self.comboBox_3.setItemText(9, _translate("Dialog", "1800"))
        self.comboBox_3.setItemText(10, _translate("Dialog", "2400"))
        self.comboBox_3.setItemText(11, _translate("Dialog", "4800"))
        self.comboBox_3.setItemText(12, _translate("Dialog", "9600"))
        self.comboBox_3.setItemText(13, _translate("Dialog", "19200"))
        self.comboBox_3.setItemText(14, _translate("Dialog", "38400"))
        self.comboBox_3.setItemText(15, _translate("Dialog", "57600"))
        self.comboBox_3.setItemText(16, _translate("Dialog", "115200"))
        self.comboBox_4.setItemText(0, _translate("Dialog", "8"))
        self.comboBox_4.setItemText(1, _translate("Dialog", "7"))
        self.comboBox_4.setItemText(2, _translate("Dialog", "6"))
        self.comboBox_5.setItemText(0, _translate("Dialog", "1"))
        self.comboBox_5.setItemText(1, _translate("Dialog", "2"))
        self.comboBox_6.setItemText(0, _translate("Dialog", "无校验"))
        self.comboBox_6.setItemText(1, _translate("Dialog", "奇校验"))
        self.comboBox_6.setItemText(2, _translate("Dialog", "偶校验"))
        self.pushButton_2.setText(_translate("Dialog", "恢复默认"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "COM1"))
