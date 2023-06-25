from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3

from tela_login import Ui_Login
from principal import Principal
import Back_Login

class Login():

    def __init__(self) -> None:
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_Login()
        self.ui.setupUi(self.MainWindow)
        self.ui.bt_entrar.clicked.connect(self.login)
        self.MainWindow.showMaximized()

    def login(self): # Função OK - Verifica o usuário ADM
        logar = self.ui.ln_login.text()
        senha = self.ui.ln_senha.text()
        log = [logar, senha]
        
        con = sqlite3.connect('./database/AvalProBD.db')

        if logar != "" and senha != "":
            with con:
                seta = con.cursor()
                sql = "SELECT Login, Senha FROM ADM"
                seta.execute(sql)
                dados = seta.fetchall()
                
            if dados[0][0] == log[0] and dados[0][1] == log[1]:
                self.sistema = Principal()
                self.MainWindow.close()
                
            else:
                QMessageBox.warning(QMessageBox(),"ALERTA","LOGIN ou SENHA INVÁLIDOS")
                self.ui.ln_login.setText("")
                self.ui.ln_senha.setText("")
        else:
            QMessageBox.warning(QMessageBox(),"ALERTA","PREENCHA OS CAMPOS VAZIOS!")
            self.ui.ln_login.setText("")
            self.ui.ln_senha.setText("")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    sistema = Login()
    app.exec()