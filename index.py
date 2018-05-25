import sys
from PyQt5.QtCore import * 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import DES_ui
import DES_tool
 
# qtCreatorFile = "./UI/DES.ui" # Enter file here.
 
# Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
Ui_MainWindow = DES_ui.Ui_MainWindow

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.Key_gen_btn.clicked.connect(self.Key_gen_btn_clicked)
        self.Encrypt_btn.clicked.connect(self.Encrypt_btn_clicked)
        self.Key_copy_btn.clicked.connect(self.Key_copy_btn_clicked)
        self.Decrypt_btn.clicked.connect(self.Decrypt_btn_clicked)

    def warning(self, content):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(content)
        # msg.setInformativeText("This is additional information")
        # msg.setWindowTitle("Warning")
        # msg.setDetailedText("The details are as follows:")
        retval = msg.exec_()        
        
    def Encrypt_btn_clicked(self):
        print ('you clicked Encrypt button')
        plain = self.Plain_text.toPlainText()
        plain = plain.replace(' ', '')
        self.Plain_text.setPlainText(plain)
        key = self.Key_text.toPlainText()
        if (plain == '' or key == ''):
            self.warning('Key is empty !')
        else:
            cipher_pack = DES_tool.encryptor(plain, key)
            self.Cipher_text.setPlainText(cipher_pack["cipher"])
            self.Addition_text.setPlainText(cipher_pack["addition"])
            self.Plain_text2.setPlainText('')
    
    def Key_gen_btn_clicked(self):
        newkey = DES_tool.keygen()
        self.Key_text.setPlainText(newkey['hex'])
        self.Cipher_text.setPlainText('')
        self.Addition_text.setPlainText('')
        self.Key_text2.setPlainText('')
        self.Plain_text2.setPlainText('')

    def Key_copy_btn_clicked(self):
        self.Key_text2.setPlainText(self.Key_text.toPlainText())
        self.Plain_text2.setPlainText('')

    def Decrypt_btn_clicked(self):
        print ('you clicked Decrypt button')
        cipher = self.Cipher_text.toPlainText()
        addition = self.Addition_text.toPlainText()
        key = self.Key_text2.toPlainText()
        if (key == ''):
            self.warning('Key is empty !')
        elif (cipher == ''):
            self.warning('Cipher is empty !')
        elif (addition == ''):
            self.addition('Addition is empty !')
        else:
            plain = DES_tool.decryptor(cipher, addition, key)
            self.Plain_text2.setPlainText(plain["plain"])
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
