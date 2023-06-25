from PyQt5 import QtCore, QtGui, QtWidgets
import Back_Editar

class Ui_Editar(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(834, 344)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-image: url(:/img/Back_Editar.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setStyleSheet("background: transparent")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_12 = QtWidgets.QWidget(self.widget)
        self.widget_12.setStyleSheet("background: transparent")
        self.widget_12.setObjectName("widget_12")
        self.label_7 = QtWidgets.QLabel(self.widget_12)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 61, 21))
        self.label_7.setStyleSheet("background-color: rgba(0, 0, 0,.7);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";\n"
"border-style: outset;\n"
"border-radius: 5px")
        self.label_7.setObjectName("label_7")
        self.ln_nome = QtWidgets.QLineEdit(self.widget_12)
        self.ln_nome.setGeometry(QtCore.QRect(10, 40, 361, 31))
        self.ln_nome.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color: black;\n"
"border-radius: 5px;\n"
"padding-left: 10px")
        self.ln_nome.setObjectName("ln_nome")
        self.verticalLayout.addWidget(self.widget_12)
        self.widget_13 = QtWidgets.QWidget(self.widget)
        self.widget_13.setStyleSheet("background: transparent")
        self.widget_13.setObjectName("widget_13")
        self.label_8 = QtWidgets.QLabel(self.widget_13)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.label_8.setStyleSheet("background-color: rgba(0, 0, 0,.7);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";\n"
"border-style: outset;\n"
"border-radius: 5px")
        self.label_8.setObjectName("label_8")
        self.ln_funcao = QtWidgets.QLineEdit(self.widget_13)
        self.ln_funcao.setGeometry(QtCore.QRect(10, 40, 361, 31))
        self.ln_funcao.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color: black;\n"
"border-radius: 5px;\n"
"padding-left: 10px")
        self.ln_funcao.setObjectName("ln_funcao")
        self.verticalLayout.addWidget(self.widget_13)
        self.widget_14 = QtWidgets.QWidget(self.widget)
        self.widget_14.setStyleSheet("background: transparent")
        self.widget_14.setObjectName("widget_14")
        self.label_9 = QtWidgets.QLabel(self.widget_14)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 101, 21))
        self.label_9.setStyleSheet("background-color: rgba(0, 0, 0,.7);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";\n"
"border-style: outset;\n"
"border-radius: 5px")
        self.label_9.setObjectName("label_9")
        self.ln_admissao = QtWidgets.QLineEdit(self.widget_14)
        self.ln_admissao.setGeometry(QtCore.QRect(10, 40, 361, 31))
        self.ln_admissao.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color: black;\n"
"border-radius: 5px;\n"
"padding-left: 10px")
        self.ln_admissao.setObjectName("ln_admissao")
        self.verticalLayout.addWidget(self.widget_14)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 2, 1)
        self.widget_2 = QtWidgets.QWidget(self.frame)
        self.widget_2.setStyleSheet("background: transparent")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_10 = QtWidgets.QWidget(self.widget_2)
        self.widget_10.setStyleSheet("background: transparent")
        self.widget_10.setObjectName("widget_10")
        self.label_6 = QtWidgets.QLabel(self.widget_10)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.label_6.setStyleSheet("background-color: rgba(0, 0, 0,.7);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";\n"
"border-style: outset;\n"
"border-radius: 5pX")
        self.label_6.setObjectName("label_6")
        self.ln_cargo = QtWidgets.QLineEdit(self.widget_10)
        self.ln_cargo.setGeometry(QtCore.QRect(10, 40, 361, 31))
        self.ln_cargo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color: black;\n"
"border-radius: 5px;\n"
"padding-left: 10px")
        self.ln_cargo.setObjectName("ln_cargo")
        self.verticalLayout_2.addWidget(self.widget_10)
        self.widget_8 = QtWidgets.QWidget(self.widget_2)
        self.widget_8.setStyleSheet("background: transparent;")
        self.widget_8.setObjectName("widget_8")
        self.label_5 = QtWidgets.QLabel(self.widget_8)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.label_5.setStyleSheet("background-color: rgba(0, 0, 0,.7);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";\n"
"border-style: outset;\n"
"border-radius: 5px")
        self.label_5.setObjectName("label_5")
        self.ln_horario = QtWidgets.QLineEdit(self.widget_8)
        self.ln_horario.setGeometry(QtCore.QRect(10, 40, 361, 31))
        self.ln_horario.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color: black;\n"
"border-radius: 5px;\n"
"padding-left: 10px")
        self.ln_horario.setObjectName("ln_horario")
        self.verticalLayout_2.addWidget(self.widget_8)
        self.gridLayout_2.addWidget(self.widget_2, 0, 1, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.frame)
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 92))
        self.widget_3.setStyleSheet("background: transparent;")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.bt_salvar = QtWidgets.QPushButton(self.widget_3)
        self.bt_salvar.setMaximumSize(QtCore.QSize(100, 50))
        self.bt_salvar.setStyleSheet("QPushButton{\n"
"    color: rgb(0, 0, 255);\n"
"    font: 75 18pt \"Arial\";\n"
"    background-color: rgb(255, 255, 0);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: blue;\n"
"    border-radius: 5px\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(0, 0, 255);\n"
"    color: rgb(255, 255, 0);\n"
"    border-color:yellow;\n"
"}")
        self.bt_salvar.setObjectName("bt_salvar")
        self.gridLayout_3.addWidget(self.bt_salvar, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget_3, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sistema de Avaliação do Profissional - SisAvalPro - Tela de ATUALIZAÇÃO DE COLABORADOR"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">NOME</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">FUNÇÃO</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">ADMISSÃO</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">CARGO</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">HORÁRIO</p></body></html>"))
        self.bt_salvar.setText(_translate("MainWindow", "SALVAR"))

# Utilizar em caso de teste

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Editar()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
