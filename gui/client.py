# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/client.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_ClientWindow(object):
    def setupUi(self, ClientWindow):
        ClientWindow.setObjectName("ClientWindow")
        ClientWindow.resize(640, 800) # 480
        self.centralwidget = QtWidgets.QWidget(ClientWindow)
        self.centralwidget.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 640, 461)) #461
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.subject_label = QtWidgets.QLabel(self.frame)
        self.subject_label.setGeometry(QtCore.QRect(10, 361, 91, 21))
        self.subject_label.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.subject_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.subject_label.setObjectName("subject_label")
        self.message_label = QtWidgets.QLabel(self.frame)
        self.message_label.setGeometry(QtCore.QRect(10, 390, 91, 61))
        self.message_label.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.message_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.message_label.setObjectName("message_label")
        self.name_label = QtWidgets.QLabel(self.frame)
        self.name_label.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.name_label.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label.setObjectName("name_label")
        self.name_text = QtWidgets.QLineEdit(self.frame)
        self.name_text.setGeometry(QtCore.QRect(80, 10, 551, 23))
        self.name_text.setObjectName("name_text")
        self.subject_text = QtWidgets.QLineEdit(self.frame)
        self.subject_text.setGeometry(QtCore.QRect(110, 361, 451, 23))
        self.subject_text.setObjectName("subject_text")
        self.message_text = QtWidgets.QPlainTextEdit(self.frame)
        self.message_text.setGeometry(QtCore.QRect(110, 391, 451, 61))
        self.message_text.setTabChangesFocus(False)
        self.message_text.setPlainText("")
        self.message_text.setObjectName("message_text")
        self.send_button = QtWidgets.QPushButton(self.frame)
        self.send_button.setGeometry(QtCore.QRect(570, 361, 61, 91))
        self.send_button.setToolTip("")
        self.send_button.setObjectName("send_button")
        self.chat_text = QtWidgets.QTextBrowser(self.frame)
        self.chat_text.setGeometry(QtCore.QRect(10, 40, 621, 311))
        self.chat_text.setObjectName("chat_text")
        ClientWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ClientWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        ClientWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ClientWindow)
        #ClientWindow.show()
        QtCore.QMetaObject.connectSlotsByName(ClientWindow)

    def retranslateUi(self, ClientWindow):
        _translate = QtCore.QCoreApplication.translate
        ClientWindow.setWindowTitle(_translate("ClientWindow", "Python Chat Client"))
        self.subject_label.setText(_translate("ClientWindow", "Destinat."))
        self.subject_text.setText(_translate("ClientWindow", "Publico"))
        self.message_label.setText(_translate("ClientWindow", "Mensagem"))
        self.name_label.setText(_translate("ClientWindow", "Nome "))
        self.name_text.setText(_translate("ClientWindow", "Polianny"))
        self.send_button.setText(_translate("ClientWindow", "Enviar"))


class ClientGUI(QtWidgets.QMainWindow):

    """Interface principal da tela de cliente."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ui = Ui_ClientWindow()
        self.ui.setupUi(self)
        self.ui.shortcut = QtWidgets.QShortcut(
            QtGui.QKeySequence("Ctrl+Return"),  # send message shortcut
            self
        )
        self.ui.message_text.setFocus()

    def closeEvent(self, event):
        # self.client_thread.closed = True
        # self.client.close()
        # parent = self.parent()
        # if not parent:
        sys.exit()

    def init_client(self):
        # self.client_thread.start()
        # self.statusBar().showMessage('oi eu sou o goku')
        self.show()

    def send(self):
        """Envia uma mensagem para o servidor como as informações da GUI"""
        subject = self.ui.subject_text.text()
        message = self.ui.message_text.toPlainText()
        name = self.ui.name_text.text()

        self.ui.message_text.clear()  # clean message_text field
        self.client.name = name


    def receive(self):
        pass
        # """Recebe uma mensagem do servidor e atualiza a interface."""
        # msg = self.client.messages.get()

        # new_msg = str(msg).split('\n')
        # #print(new_msg)
        # del new_msg[2]
        # #print(new_msg)
        # _messagem = new_msg[2].split('@')[0]
        # print(_messagem.split("\""))
        # _messagem = _messagem.split("\"")[1]
        # _key = new_msg[2].split('@')[1]
        # msg_deciph = cifrador._decrypt(_messagem, _key)
        # #print(msg_deciph.decode("utf-8"))
        # _messagem = msg_deciph.decode("utf-8")
        # m = f"\n{new_msg[0]}\n{new_msg[1]}\nMensagem: {_messagem}\n{new_msg[3]}\n"

        # self.ui.chat_text.insertPlainText(m)
        # self.ui.chat_text.moveCursor(QtGui.QTextCursor.End)
        # self.ui.chat_text.ensureCursorVisible()

    def critical_error(self, msg):
        """Erro crítico: servidor está morto. Deve finalizar a aplicação com um aviso."""
        dlg = QtWidgets.QMessageBox()
        dlg.setWindowTitle("Uma merda enorme aconteceu!")
        dlg.setIcon(QtWidgets.QMessageBox.Critical)
        dlg.setText(msg)
        dlg.exec_()
        self.close()

    @classmethod
    def run(cls):
        """Inicializa a interface do sistema apropriadamente"""
        app = QtWidgets.QApplication(sys.argv)
        main = cls()
        main.init_client()
        sys.exit(app.exec_())

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon

class Login(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 input dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        
    
    def initUI(self):
        # self.setWindowTitle(self.title)
        # self.setGeometry(self.left, self.top, self.width, self.height)
        try:
            self.getText()
        except:
            print('Erro: fechei a tela de login')
    
        # self.show()

    def getText(self):
        text, okPressed = QInputDialog.getText(self, "Nome","Digite seu nome:", QLineEdit.Normal, "")
        if okPressed and text != '':
            print(text)
            return text

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Login()
    sys.exit(app.exec_())
    ClientGUI.run()

