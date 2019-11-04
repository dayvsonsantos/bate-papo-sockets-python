# coding: utf-8

"""
Tela de integração com server.py e client.py.

Permite disparar N servidores e N clientes, onde HOST e PORT
é parametrizado.
"""

from PyQt5 import QtWidgets
import gui.main
import servidor
import sys
# import client
# import server
# import protocol

HOST = "127.0.0.1"
PORT = 9999

class MainGUI(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = gui.main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.client_button.clicked.connect(self.open_client)
        self.ui.server_button.clicked.connect(self.open_server)
        self.ui.host_text.setText(HOST)
        self.ui.port_text.setText(str(PORT))

    def update_host_port(self):
        HOST = self.ui.host_text.text()
        PORT = int(self.ui.port_text.text())

    def open_server(self):
        self.update_host_port()
        s = servidor.ServerGUI(parent=self)
        s.init_server()

    def open_client(self):
        self.update_host_port()
        c = client.ClientGUI(parent=self)
        c.init_client()

    @classmethod
    def run(cls):
        app = QtWidgets.QApplication(sys.argv)
        main = cls()
        main.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    MainGUI.run()
