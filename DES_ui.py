# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/DES.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(659, 587)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Encrypt_btn = QtGui.QPushButton(self.centralwidget)
        self.Encrypt_btn.setGeometry(QtCore.QRect(540, 200, 89, 25))
        self.Encrypt_btn.setObjectName(_fromUtf8("Encrypt_btn"))
        self.Decrypt_btn = QtGui.QPushButton(self.centralwidget)
        self.Decrypt_btn.setGeometry(QtCore.QRect(540, 400, 89, 25))
        self.Decrypt_btn.setObjectName(_fromUtf8("Decrypt_btn"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 67, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 170, 67, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 230, 67, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.Key_text = QtGui.QPlainTextEdit(self.centralwidget)
        self.Key_text.setGeometry(QtCore.QRect(150, 170, 361, 31))
        self.Key_text.setObjectName(_fromUtf8("Key_text"))
        self.Plain_text = QtGui.QPlainTextEdit(self.centralwidget)
        self.Plain_text.setGeometry(QtCore.QRect(150, 30, 361, 111))
        self.Plain_text.setObjectName(_fromUtf8("Plain_text"))
        self.Key_gen_btn = QtGui.QPushButton(self.centralwidget)
        self.Key_gen_btn.setGeometry(QtCore.QRect(540, 140, 89, 25))
        self.Key_gen_btn.setObjectName(_fromUtf8("Key_gen_btn"))
        self.Cipher_text = QtGui.QPlainTextEdit(self.centralwidget)
        self.Cipher_text.setGeometry(QtCore.QRect(150, 230, 361, 111))
        self.Cipher_text.setObjectName(_fromUtf8("Cipher_text"))
        self.Plain_text2 = QtGui.QPlainTextEdit(self.centralwidget)
        self.Plain_text2.setGeometry(QtCore.QRect(150, 430, 361, 111))
        self.Plain_text2.setObjectName(_fromUtf8("Plain_text2"))
        self.Key_text2 = QtGui.QPlainTextEdit(self.centralwidget)
        self.Key_text2.setGeometry(QtCore.QRect(150, 370, 361, 31))
        self.Key_text2.setObjectName(_fromUtf8("Key_text2"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 370, 67, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 430, 67, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.Key_copy_btn = QtGui.QPushButton(self.centralwidget)
        self.Key_copy_btn.setGeometry(QtCore.QRect(540, 340, 89, 25))
        self.Key_copy_btn.setObjectName(_fromUtf8("Key_copy_btn"))
        self.Addition_text = QtGui.QTextEdit(self.centralwidget)
        self.Addition_text.setGeometry(QtCore.QRect(550, 260, 51, 31))
        self.Addition_text.setObjectName(_fromUtf8("Addition_text"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(550, 300, 67, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "DES工具", None))
        self.Encrypt_btn.setText(_translate("MainWindow", "加密", None))
        self.Decrypt_btn.setText(_translate("MainWindow", "解密", None))
        self.label.setText(_translate("MainWindow", "明文", None))
        self.label_2.setText(_translate("MainWindow", "加密密钥", None))
        self.label_3.setText(_translate("MainWindow", "密文", None))
        self.Key_gen_btn.setText(_translate("MainWindow", "生成密钥", None))
        self.label_4.setText(_translate("MainWindow", "解密密钥", None))
        self.label_5.setText(_translate("MainWindow", "明文", None))
        self.Key_copy_btn.setText(_translate("MainWindow", "复制密钥", None))
        self.label_6.setText(_translate("MainWindow", "补充位数", None))

