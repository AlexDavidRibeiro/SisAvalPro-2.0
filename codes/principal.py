from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3

from tela_principal import Ui_Principal
from avaliar import Avaliar
from editar import Editar
from arquivoPDF import regPDF

# Classe da tela principal

class Principal():

    def __init__(self) -> None:
        self.MainWindow = QtWidgets.QMainWindow()
        self.main = Ui_Principal()
        self.main.setupUi(self.MainWindow)
        self.main.bt_avaliar.clicked.connect(self.avaliar)
        self.main.bt_editar.clicked.connect(self.editar)
        self.main.bt_excluir.clicked.connect(self.excluir)
        self.main.bt_cadastrar.clicked.connect(self.cadastrar)
        self.main.bt_exit.clicked.connect(self.sair)
        self.exibe_registros()      
        self.MainWindow.showMaximized()

    def avaliar(self): # Função OK - Avalia e gera o documento
        aval = self.main.tabela_colab.currentRow()

        if aval == -1:
            QMessageBox.warning(QMessageBox(),"OBRIGATÓRIO","SELECIONE UMA LINHA!")
        else:
            con = sqlite3.connect('./database/AvalProBD.db')

            with con:            
                seta = con.cursor()
                sql = "SELECT ID FROM Colaborador"
                seta.execute(sql)
                dados = seta.fetchall() 
                id = dados[aval][0] 
                sql = "SELECT Nome FROM Colaborador WHERE ID=?"
                seta.execute(sql,[str(id)])           
                data = seta.fetchall()
                nome = str(data[0][0])
           
            regPDF.usuario(nome)
            self.sistema = Avaliar()
            self.sistema.label(nome)

    def editar(self): # Função OK - Altera dados do cadastro
        select = self.main.tabela_colab.currentRow() # Faz a leitura da linha do elemento
        
        if select == -1:
            QMessageBox.warning(QMessageBox(),"OBRIGATÓRIO","SELECIONE UMA LINHA!")
        else:
            Editar.start(select)
            self.sistema = Editar(self.exibe_registros)

    def excluir(self): # Função OK - Exclui registro de cadastro
        select = self.main.tabela_colab.currentRow() # Faz a leitura da linha do elemento
        
        if select == -1:
            QMessageBox.warning(QMessageBox(),"OBRIGATÓRIO","SELECIONE UMA LINHA!")
        else:
            resp = QMessageBox.question(QMessageBox(),"ALERTA - EXCLUSÃO DE CADASTRO","Deseja realmente excluir este colaborador(a) do cadastro?",
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            
            if resp == QMessageBox.Yes:
                con = sqlite3.connect('./database/AvalProBD.db')
        
                with con:
                    seta = con.cursor()
                    sql = "SELECT ID FROM Colaborador"
                    seta.execute(sql)
                    dados = seta.fetchall()
                    id = dados[select][0]
                    sql = "DELETE FROM Colaborador WHERE ID=?" # Deleta a linha toda pelo ID
                    seta.execute(sql,[str(id)])

                self.main.tabela_colab.removeRow(select)
                QMessageBox.information(QMessageBox(),"CONFIRMAÇÃO","Cadastro removido com sucesso!")
                print("Exclusão de cadastro executada")

    def sair(self): # Função OK - Encerra o sistema
        self.MainWindow.close()
        print("Sistema encerrado")

    def cadastrar(self): # Função OK - Cadastra o(a) colaborador(a)
        nome = self.main.ln_nome.text()
        cargo = self.main.ln_cargo.text()
        funcao = self.main.ln_funcao.text()
        horario = self.main.ln_horario.text()
        admissao = self.main.ln_admissao.text()

        if nome != "" and cargo != "" and funcao != "" and horario != "" and admissao != "":
            
            data = [nome,cargo,funcao,horario,admissao]

            con = sqlite3.connect('./database/AvalProBD.db')

            with con:
                seta = con.cursor()
                sql = "INSERT INTO Colaborador (Nome, Cargo, Função, Horário, Admissão) VALUES (?,?,?,?,?)"
                seta.execute(sql,data)

                nome = self.main.ln_nome.setText("")
                cargo = self.main.ln_cargo.setText("")
                funcao = self.main.ln_funcao.setText("")
                horario = self.main.ln_horario.setText("")
                admissao = self.main.ln_admissao.setText("")

            self.exibe_registros()

        else:
            QMessageBox.warning(QMessageBox(),"ATENÇÃO","AINDA EXISTEM CAMPOS VAZIOS!")

    def exibe_registros(self): # Função OK - Exibe os Registros
     
        con = sqlite3.connect('./database/AvalProBD.db')

        with con:
            seta = con.cursor()
            sql = "SELECT * FROM Colaborador"
            seta.execute(sql)
            dados = seta.fetchall()
            self.main.tabela_colab.setRowCount(len(dados))
            self.main.tabela_colab.setColumnCount(6)

            for linha in range (0, len(dados)): # Loop que organiza os dados para exibição
                for coluna in range (0,6):
                    self.main.tabela_colab.setItem(linha,coluna,QtWidgets.QTableWidgetItem(str(dados[linha][coluna])))
