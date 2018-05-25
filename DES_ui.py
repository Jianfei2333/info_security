# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DES.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(659, 587)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Encrypt_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Encrypt_btn.setGeometry(QtCore.QRect(540, 200, 89, 25))
        self.Encrypt_btn.setObjectName("Encrypt_btn")
        self.Decrypt_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Decrypt_btn.setGeometry(QtCore.QRect(540, 400, 89, 25))
        self.Decrypt_btn.setObjectName("Decrypt_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 170, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 230, 67, 17))
        self.label_3.setObjectName("label_3")
        self.Key_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Key_text.setGeometry(QtCore.QRect(150, 170, 361, 31))
        self.Key_text.setObjectName("Key_text")
        self.Plain_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Plain_text.setGeometry(QtCore.QRect(150, 30, 361, 111))
        self.Plain_text.setObjectName("Plain_text")
        self.Key_gen_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Key_gen_btn.setGeometry(QtCore.QRect(540, 140, 89, 25))
        self.Key_gen_btn.setObjectName("Key_gen_btn")
        self.Cipher_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Cipher_text.setGeometry(QtCore.QRect(150, 230, 361, 111))
        self.Cipher_text.setObjectName("Cipher_text")
        self.Plain_text2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Plain_text2.setGeometry(QtCore.QRect(150, 430, 361, 111))
        self.Plain_text2.setObjectName("Plain_text2")
        self.Key_text2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Key_text2.setGeometry(QtCore.QRect(150, 370, 361, 31))
        self.Key_text2.setObjectName("Key_text2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 370, 67, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 430, 67, 17))
        self.label_5.setObjectName("label_5")
        self.Key_copy_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Key_copy_btn.setGeometry(QtCore.QRect(540, 340, 89, 25))
        self.Key_copy_btn.setObjectName("Key_copy_btn")
        self.Addition_text = QtWidgets.QTextEdit(self.centralwidget)
        self.Addition_text.setGeometry(QtCore.QRect(550, 260, 51, 31))
        self.Addition_text.setObjectName("Addition_text")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(550, 300, 67, 17))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DES工具"))
        self.Encrypt_btn.setText(_translate("MainWindow", "加密"))
        self.Decrypt_btn.setText(_translate("MainWindow", "解密"))
        self.label.setText(_translate("MainWindow", "明文"))
        self.label_2.setText(_translate("MainWindow", "加密密钥"))
        self.label_3.setText(_translate("MainWindow", "密文"))
        self.Key_gen_btn.setText(_translate("MainWindow", "生成密钥"))
        self.label_4.setText(_translate("MainWindow", "解密密钥"))
        self.label_5.setText(_translate("MainWindow", "明文"))
        self.Key_copy_btn.setText(_translate("MainWindow", "复制密钥"))
        self.label_6.setText(_translate("MainWindow", "补充位数"))

