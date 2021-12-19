# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog
from speed_ui import Ui_Dialog as Speed_Ui_Dialog
from UART_ui import Ui_Dialog as UART_Ui_Dialog
from uart_parse import UARTParser, get_uart_default_settings
from draw_figure import SpeedFigure, TemperatureFigure

REFRESH_TIME = 1000
DATA_LIST_LIMIT = 30


class Ui_Form(QtWidgets.QMainWindow):
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

    def setupUi(self):
        Form = self
        Form.setObjectName("Form")
        Form.resize(1302, 958)
        self.label = QtWidgets.QLabel(Form)

        self.setWindowFlags(Qt.FramelessWindowHint)  # 去边框
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        self.setWindowIcon(QIcon(".\\Assests/icon.jpg"))

        self.label.setGeometry(QtCore.QRect(90, 40, 1161, 801))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(".\\Assests/background.webp"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(380, 570, 171, 41))
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "    color:White;\n"
                                      "    border-radius: 7px;\n"
                                      "    font-family:微软雅黑;\n"
                                      "    background:#6633FF;\n"
                                      "    border:1px;\n"
                                      "    font-size:16px;\n"
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
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(1071, 130, 31, 31))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "    background:#6C6C6C;\n"
                                        "    color:white;\n"
                                        "    font-size:18px;\n"
                                        "    border-radius: 12px;\n"
                                        "    font-family: Consolas;\n"
                                        "}\n"
                                        "QPushButton:hover{                    \n"
                                        "    background:#9D9D9D;\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    border: 1px solid #3C3C3C!important;\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(1120, 130, 31, 31))
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
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(320, 278, 111, 31))
        self.label_2.setStyleSheet("QLabel{\n"
                                   "    background:#6C6C6C;\n"
                                   "    color:white;\n"
                                   "    font-size:16px;\n"
                                   "    border-radius:\n"
                                   "    8px;font-family: 微软雅黑;\n"
                                   "}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(380, 640, 171, 41))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
                                        "    color:White;\n"
                                        "    border-radius: 7px;\n"
                                        "    font-family:微软雅黑;\n"
                                        "    background:#6633FF;\n"
                                        "    border:1px;\n"
                                        "    font-size:16px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    background:#6666FF;\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    background:#6600FF;\n"
                                        "}")
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(870, 180, 111, 31))
        self.label_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_3.setStyleSheet("QLabel{\n"
                                   "    background:#6C6C6C;\n"
                                   "    color:white;\n"
                                   "    font-size:16px;\n"
                                   "    border-radius:\n"
                                   "    8px;font-family: 微软雅黑;\n"
                                   "}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(770, 220, 321, 231))
        self.graphicsView.setStyleSheet("QGraphicsView{"
                                        "padding:0px;border:0px"
                                        "}")
        self.graphicsView.setObjectName("graphicsView")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(320, 388, 111, 31))
        self.label_6.setStyleSheet("QLabel{\n"
                                   "    background:#6C6C6C;\n"
                                   "    color:white;\n"
                                   "    font-size:16px;\n"
                                   "    border-radius:\n"
                                   "    8px;font-family: 微软雅黑;\n"
                                   "}")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(870, 460, 111, 31))
        self.label_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_5.setStyleSheet("QLabel{\n"
                                   "    background:#6C6C6C;\n"
                                   "    color:white;\n"
                                   "    font-size:16px;\n"
                                   "    border-radius:\n"
                                   "    8px;font-family: 微软雅黑;\n"
                                   "}")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.graphicsView_2 = QtWidgets.QGraphicsView(Form)
        self.graphicsView_2.setGeometry(QtCore.QRect(770, 500, 321, 231))
        self.graphicsView_2.setStyleSheet("QGraphicsView{"
                                          "padding:0px;border:0px"
                                          "}")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(190, 130, 41, 41))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(".\\Assests/icon.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(490, 260, 131, 51))
        self.label_7.setStyleSheet("QLabel{\n"
                                   "    background:#FFFFFF;\n"
                                   "    color:black;\n"
                                   "    font-size:48px;\n"
                                   "    border-radius:\n"
                                   "    8px;font-family: Microsoft YaHei UI;\n"
                                   "}")
        self.label_7.setAlignment(QtCore.Qt.AlignRight)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(490, 370, 131, 51))
        self.label_8.setStyleSheet("QLabel{\n"
                                   "    background:#FFFFFF;\n"
                                   "    color:black;\n"
                                   "    font-size:48px;\n"
                                   "    border-radius:\n"
                                   "    8px;font-family: Microsoft YaHei UI;\n"
                                   "}")
        self.label_8.setAlignment(QtCore.Qt.AlignRight)
        self.label_8.setObjectName("label_8")
        self.label.raise_()
        self.label_3.raise_()
        self.graphicsView.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.label_2.raise_()
        self.pushButton_4.raise_()
        self.label_6.raise_()
        self.label_5.raise_()
        self.graphicsView_2.raise_()
        self.label_4.raise_()
        self.label_7.raise_()
        self.label_8.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton_2.clicked.connect(self.showMinimized)
        self.pushButton_3.clicked.connect(self.close)

        self.pushButton.clicked.connect(self.to_speed_settings)
        self.pushButton_4.clicked.connect(self.to_uart_settings)

        self.startTimer(REFRESH_TIME)
        self.uart_parser = UARTParser(*get_uart_default_settings())

        self.speed_list = []
        self.temperature_list = []
        self.speed_graphicscene = QtWidgets.QGraphicsScene()
        self.temperature_graphicscene = QtWidgets.QGraphicsScene()

    def timerEvent(self, event: 'QTimerEvent') -> None:
        self.uart_parser.get_data()
        _translate = QtCore.QCoreApplication.translate
        self.label_7.setText(_translate(
            "Form", f"{self.uart_parser.temperature}°C"))
        self.label_8.setText(_translate("Form", f"{self.uart_parser.speed} %"))

        self.speed_list.append(self.uart_parser.speed)
        self.temperature_list.append(self.uart_parser.temperature)
        if len(self.speed_list) > DATA_LIST_LIMIT:
            self.speed_list.pop(0)
            self.temperature_list.pop(0)

        speed_figure = SpeedFigure()
        speed_figure.display(self.speed_list)
        self.speed_graphicscene.addWidget(speed_figure)
        self.graphicsView_2.setScene(self.speed_graphicscene)
        self.graphicsView_2.show()

        temperature_figure = TemperatureFigure()
        temperature_figure.display(self.temperature_list)
        self.temperature_graphicscene.addWidget(temperature_figure)
        self.graphicsView.setScene(self.temperature_graphicscene)
        self.graphicsView.show()

        return super().timerEvent(event)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "转速和定时设定"))
        self.pushButton_2.setText(_translate("Form", "-"))
        self.pushButton_3.setText(_translate("Form", "X"))
        self.label_2.setText(_translate("Form", "实时温度"))
        self.pushButton_4.setText(_translate("Form", "串口设定"))
        self.label_3.setText(_translate("Form", "温度曲线"))
        self.label_6.setText(_translate("Form", "实时转速"))
        self.label_5.setText(_translate("Form", "转速曲线"))
        self.label_7.setText(_translate("Form", "°C"))
        self.label_8.setText(_translate("Form", "%"))

    def to_uart_settings(self):
        self.uart_dialog = UART_Ui_Dialog()
        self.uart_dialog.setupUi(self.uart_parser)
        self.uart_dialog.show()

    def to_speed_settings(self):
        self.speed_dialog = Speed_Ui_Dialog()
        self.speed_dialog.setupUi(self.uart_parser)
        self.speed_dialog.show()
