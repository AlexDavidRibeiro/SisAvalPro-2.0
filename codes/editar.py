from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3

from tela_editar import Ui_Editar

class Editar():

    def start(x): # Função que recebe o valor da linha
        global select
        select = x

    def __init__(self,exibe_registros) -> None:
        self.MainWindow = QtWidgets.QMainWindow()
        self.edit = Ui_Editar()
        self.edit.setupUi(self.MainWindow)
        self.exibe = exibe_registros
        self.edit.bt_salvar.clicked.connect(self.editar)
        self.MainWindow.show()

        con = sqlite3.connect('./database/AvalProBD.db')

        with con:
            global select
            global numID
            seta = con.cursor()
            sql = "SELECT ID FROM Colaborador" # Seleciona a coluna ID da tabela
            seta.execute(sql)
            dados = seta.fetchall()
            id = dados[select][0]     # Armazena o ID da linha selecionada
            sql = "SELECT * FROM Colaborador WHERE ID=?" # Seleciona a linha toda pelo ID
            seta.execute(sql,[str(id)])
            colab = seta.fetchall()
            
            self.edit.ln_nome.setText(str(colab[0][1]))
            self.edit.ln_cargo.setText(str(colab[0][2]))
            self.edit.ln_funcao.setText(str(colab[0][3]))
            self.edit.ln_horario.setText(str(colab[0][4]))
            self.edit.ln_admissao.setText(str(colab[0][5]))

        numID = id

    def editar(self): # Função que realiza a atualização do registro
                
        global numID
        
        nome = self.edit.ln_nome.text()
        cargo = self.edit.ln_cargo.text()    
        funcao = self.edit.ln_funcao.text()    
        horario = self.edit.ln_horario.text()    
        admissao = self.edit.ln_admissao.text()    
        
        listaEdit = [nome,cargo,funcao,horario,admissao, numID]
        
        con = sqlite3.connect('./database/AvalProBD.db')

        with con: 
            seta = con.cursor()
            sql = "UPDATE Colaborador SET Nome=?, Cargo=?, Função=?, Horário=?, Admissão=? WHERE ID=?"
            seta.execute(sql,listaEdit) # Executa e armazena as alterações feitas

        QMessageBox.information(QMessageBox(),"DADOS SALVOS","Alterações salvas com sucesso!")
        self.MainWindow.close()
        self.exibe()
        print("Execução de alteração de dados")