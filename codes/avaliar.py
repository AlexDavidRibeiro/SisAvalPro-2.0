from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox

from tela_aval import Ui_Aval
from arquivoPDF import regPDF

class Avaliar():
    def __init__(self) -> None:
        self.MainWindow = QtWidgets.QMainWindow()
        self.aval = Ui_Aval()
        self.aval.setupUi(self.MainWindow)
        
        # Botões Emojis de PONTUALIDADE
        self.aval.pontu_triste.clicked.connect(lambda:self.pontu(1.1))
        self.aval.pontu_neutro.clicked.connect(lambda:self.pontu(1.2))
        self.aval.pontu_feliz.clicked.connect(lambda:self.pontu(1.3))

        # Botões Emojis de EXPERIÊNCIA
        self.aval.expe_triste.clicked.connect(lambda:self.expe(2.1))
        self.aval.expe_neutro.clicked.connect(lambda:self.expe(2.2))
        self.aval.expe_feliz.clicked.connect(lambda:self.expe(2.3))

        # Botões Emojis de ATENDIMENTO
        self.aval.atendi_triste.clicked.connect(lambda:self.atendi(3.1))
        self.aval.atendi_neutro.clicked.connect(lambda:self.atendi(3.2))
        self.aval.atendi_feliz.clicked.connect(lambda:self.atendi(3.3))

        # Botões Emojis de PROATIVIDADE
        self.aval.proativi_triste.clicked.connect(lambda:self.proa(4.1))
        self.aval.proativi_neutro.clicked.connect(lambda:self.proa(4.2))
        self.aval.proativi_feliz.clicked.connect(lambda:self.proa(4.3))

        # Botões Emojis de DINÂMICA
        self.aval.dina_triste.clicked.connect(lambda:self.dina(5.1))
        self.aval.dina_neutro.clicked.connect(lambda:self.dina(5.2))
        self.aval.dina_feliz.clicked.connect(lambda:self.dina(5.3))

        # Botões Emojis de TECNOLOGIA
        self.aval.tecnol_triste.clicked.connect(lambda:self.tecnol(6.1))
        self.aval.tecnol_neutro.clicked.connect(lambda:self.tecnol(6.2))
        self.aval.tecnol_feliz.clicked.connect(lambda:self.tecnol(6.3))

        # Botões Emojis de ASSIDUIDADE
        self.aval.assidu_triste.clicked.connect(lambda:self.assidu(7.1))
        self.aval.assidu_neutro.clicked.connect(lambda:self.assidu(7.2))
        self.aval.assidu_feliz.clicked.connect(lambda:self.assidu(7.3))

        self.aval.bt_relatorio.clicked.connect(self.texto)
        self.MainWindow.showMaximized()

    def pontu(self, pnt): # Função OK
        match pnt:
            case 1.1:
                self.aval.lb_pontu.setPixmap(QtGui.QPixmap('icons/triste.png'))
                pt = "O(A) colaborador(a) possui algum(ns) atraso(s) e, mesmo sedo orientado, continua se atrasando."
                regPDF.resPontu(pt)
            case 1.2:
                self.aval.lb_pontu.setPixmap(QtGui.QPixmap('icons/neutro.png'))
                pt = "O colaborador é pontual e cumpre seu horário regularmente."
                regPDF.resPontu(pt)
            case 1.3:
                self.aval.lb_pontu.setPixmap(QtGui.QPixmap('icons/feliz.png'))
                pt = "O colaborador chega sempre 10 (dez) minutos mais cedo no serviço para evitar qualquer tipo de atraso."
                regPDF.resPontu(pt)

    def expe(self, ex): # Função OK
        match ex:
            case 2.1:
                self.aval.lb_expe.setPixmap(QtGui.QPixmap('icons/triste.png'))
                exp = "Ainda não adquiriu a experiência necessária para a sua função, mas se esforça em melhorar."
                regPDF.resExpe(exp)
            case 2.2:
                self.aval.lb_expe.setPixmap(QtGui.QPixmap('icons/neutro.png'))
                exp = "Possui experiência em sua função e cumpre suas atividades regularmente."
                regPDF.resExpe(exp)
            case 2.3:
                self.aval.lb_expe.setPixmap(QtGui.QPixmap('icons/feliz.png'))
                exp = "Possui experiência e habilidades que lhe favorecem positivamente, além de contribuir para o desenvolvimento profissional de seus colegas."
                regPDF.resExpe(exp)

    def atendi(self, at): # Função OK
        match at:
            case 3.1:
                self.aval.lb_atendi.setPixmap(QtGui.QPixmap('icons/triste.png'))
                atd = "Existem falhas pontuais que necessitam serem melhoradas para que possa realizar um melhor atendimento aos pacientes."
                regPDF.resAtendi(atd)
            case 3.2:
                self.aval.lb_atendi.setPixmap(QtGui.QPixmap('icons/neutro.png'))
                atd = "Consegue desempenhar sua função normalmente sem comprometer a imagem da clínica."
                regPDF.resAtendi(atd)
            case 3.3:
                self.aval.lb_atendi.setPixmap(QtGui.QPixmap('icons/feliz.png'))
                atd = "Desempenha sua função com louvor e auxilia na melhora do atendimento de seus colegas."
                regPDF.resAtendi(atd)

    def proa(self, pr): # Função OK
        match pr:
            case 4.1:
                self.aval.lb_proativi.setPixmap(QtGui.QPixmap('icons/triste.png'))
                pro = "Ainda não conseguiu adquirir a percepção funcional necessária para a execução de suas tarefas."
                regPDF.resProativi(pro)
            case 4.2:
                self.aval.lb_proativi.setPixmap(QtGui.QPixmap('icons/neutro.png'))
                pro = "Sua percepção funcional é normal e realiza suas tarefas sem a necessidade de solicitar por isso."
                regPDF.resProativi(pro)
            case 4.3:
                self.aval.lb_proativi.setPixmap(QtGui.QPixmap('icons/feliz.png'))
                pro = "Possui percepção aguçada, entendendo o momento necessário de se anteceder e resolver aos contratempos rotineiros que surgem."
                regPDF.resProativi(pro)

    def dina(self, dn): # Função OK
        match dn:
            case 5.1:
                self.aval.lb_dina.setPixmap(QtGui.QPixmap('icons/triste.png'))
                dina = "A sua dinâmica profissional ainda não atende aos requisitos necessários para um melhor desenvolvimento de suas funções."
                regPDF.resDina(dina)
            case 5.2:
                self.aval.lb_dina.setPixmap(QtGui.QPixmap('icons/neutro.png'))
                dina = "A sua dinâmica profissional é normal e executa suas atividades com destreza."
                regPDF.resDina(dina)
            case 5.3:
                self.aval.lb_dina.setPixmap(QtGui.QPixmap('icons/feliz.png'))
                dina = "A sua dinâmica profissional é acima da média, pois executa suas atividades com empenho, agilidade e dedicação."
                regPDF.resDina(dina)
    
    def tecnol(self, tec): # Função OK
        match tec:
            case 6.1:
                self.aval.lb_tecnol.setPixmap(QtGui.QPixmap('icons/triste.png'))
                tecnol = "O seu conhecimento sobre tecnologia ou nossos selfs tecnológicos ainda lhe traz alguma(s) dificuldade(s)."
                regPDF.resTecnol(tecnol)
            case 6.2:
                self.aval.lb_tecnol.setPixmap(QtGui.QPixmap('icons/neutro.png'))
                tecnol = "O seu conhecimento tecnológico atende e supre as necessidades funcionais da clínica."
                regPDF.resTecnol(tecnol)
            case 6.3:
                self.aval.lb_tecnol.setPixmap(QtGui.QPixmap('icons/feliz.png'))
                tecnol = "Possui conhecimentos tecnológicos que suprem e agregam nas suas funções."
                regPDF.resTecnol(tecnol)

    def assidu(self, assi): # Função OK
        match assi:
            case 7.1:
                self.aval.lb_assidu.setPixmap(QtGui.QPixmap('icons/triste.png'))
                assidu = "Possui alguma(s) dificuldade(s) em cumprir alguma(s) de sua(s) função(ões) para a qual foi designada com a mesma constância."
                regPDF.resAssidu(assidu)
            case 7.2:
                self.aval.lb_assidu.setPixmap(QtGui.QPixmap('icons/neutro.png'))
                assidu = "Consegue manter sua assiduidade dentro da empresa."
                regPDF.resAssidu(assidu)
            case 7.3:
                self.aval.lb_assidu.setPixmap(QtGui.QPixmap('icons/feliz.png'))
                assidu = "Muito assiduo e comprometido com suas funções e estando sempre pronto a ajudar em qualquer situação profissional."
                regPDF.resAssidu(assidu)

    def texto(self): # Função OK - Insere o relatório no documento
        txt = self.aval.rel_supervisor.toPlainText()
        regPDF.supervisor(txt)
        QMessageBox.information(QMessageBox(),"Documento Gerado com Sucesso", "Sua avaliação já está disponível na pasta 'arquivos'!")
        self.MainWindow.close()

    def label(self,nome): # Função OK - Insere o nome do avaliado na tela avaliar
        self.aval.lb_nomeColab.setText(nome)