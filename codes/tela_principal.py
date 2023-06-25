from PyQt5 import QtCore, QtGui, QtWidgets
import Back_Principal

class Ui_Principal(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(815, 620)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-image: url(:/img/Back_Principal.png);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color: white;\n"
"border-radius: 5px")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fr_high = QtWidgets.QFrame(self.frame)
        self.fr_high.setMaximumSize(QtCore.QSize(16777215, 300))
        self.fr_high.setStyleSheet("background: transparent;\n"
"border-style: outset;\n"
"background-color: rgba(0, 0, 0,0.3);\n"
"border-width: 2px;\n"
"border-color: white;\n"
"border-radius: 10px")
        self.fr_high.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_high.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_high.setObjectName("fr_high")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fr_high)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabela_colab = QtWidgets.QTableWidget(self.fr_high)
        self.tabela_colab.setMaximumSize(QtCore.QSize(920, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tabela_colab.setFont(font)
        self.tabela_colab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabela_colab.setStyleSheet("background: transparent;\n"
"background-color: rgba(255, 255, 255,.7);\n"
"border-width: 1px;\n"
"border-color: black;\n"
"border-radius: 5px")
        self.tabela_colab.setObjectName("tabela_colab")
        self.tabela_colab.setColumnCount(6)
        self.tabela_colab.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        item.setFont(font)
        self.tabela_colab.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        item.setFont(font)
        self.tabela_colab.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        item.setFont(font)
        self.tabela_colab.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        item.setFont(font)
        self.tabela_colab.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        item.setFont(font)
        self.tabela_colab.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        item.setFont(font)
        self.tabela_colab.setHorizontalHeaderItem(5, item)
        self.tabela_colab.setColumnHidden(0,True)
        self.tabela_colab.horizontalHeader().setDefaultSectionSize(180)
        self.horizontalLayout.addWidget(self.tabela_colab)
        self.widget = QtWidgets.QWidget(self.fr_high)
        self.widget.setMaximumSize(QtCore.QSize(150, 16777215))
        self.widget.setStyleSheet("background: transparent;\n"
"border-style: outset;\n"
"border-width: 0;\n"
"")
        self.widget.setObjectName("widget")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.bt_avaliar = QtWidgets.QPushButton(self.widget)
        self.bt_avaliar.setMaximumSize(QtCore.QSize(80, 30))
        self.bt_avaliar.setStyleSheet("QPushButton{\n"
"    background: transparent;\n"
"    background-color: rgb(85, 170, 255);\n"
"    font: 75 12pt \"Arial\";\n"
"    color: rgb(255, 255, 255);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: white;\n"
"    border-radius: 5px;\n"
"    padding: 5px\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.bt_avaliar.setObjectName("bt_avaliar")
        self.gridLayout_9.addWidget(self.bt_avaliar, 0, 0, 1, 1)
        self.bt_editar = QtWidgets.QPushButton(self.widget)
        self.bt_editar.setMaximumSize(QtCore.QSize(80, 30))
        self.bt_editar.setStyleSheet("QPushButton{\n"
"    background: transparent;\n"
"    background-color: rgb(230, 230, 0);\n"
"    font: 75 12pt \"Arial\";\n"
"    color: rgb(255, 255, 255);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: white;\n"
"    border-radius: 5px;\n"
"    padding: 5px\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(255,255,0);\n"
"}")
        self.bt_editar.setObjectName("bt_editar")
        self.gridLayout_9.addWidget(self.bt_editar, 1, 0, 1, 1)
        self.bt_excluir = QtWidgets.QPushButton(self.widget)
        self.bt_excluir.setMaximumSize(QtCore.QSize(80, 30))
        self.bt_excluir.setStyleSheet("QPushButton{\n"
"    background: transparent;\n"
"    background-color: rgb(255, 0, 0);\n"
"    font: 75 12pt \"Arial\";\n"
"    color: rgb(255, 255, 255);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: white;\n"
"    border-radius: 5px;\n"
"    padding: 5px\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);\n"
"}")
        self.bt_excluir.setObjectName("bt_excluir")
        self.gridLayout_9.addWidget(self.bt_excluir, 2, 0, 1, 1)
        self.horizontalLayout.addWidget(self.widget)
        self.verticalLayout.addWidget(self.fr_high)
        self.fr_low = QtWidgets.QFrame(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fr_low.setFont(font)
        self.fr_low.setStyleSheet("background: transparent;\n"
"border-width:0")
        self.fr_low.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_low.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_low.setObjectName("fr_low")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.fr_low)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.fr_low)
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fr_inside_3 = QtWidgets.QFrame(self.frame_2)
        self.fr_inside_3.setMaximumSize(QtCore.QSize(620, 16777215))
        self.fr_inside_3.setStyleSheet("")
        self.fr_inside_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_inside_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_inside_3.setObjectName("fr_inside_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.fr_inside_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3.addWidget(self.fr_inside_3)
        self.fr_inside = QtWidgets.QFrame(self.frame_2)
        self.fr_inside.setMaximumSize(QtCore.QSize(620, 16777215))
        self.fr_inside.setStyleSheet("border-style: outset;\n"
"background-color: rgba(0, 0, 0,0.3);\n"
"border-width: 2px;\n"
"border-color: white;\n"
"border-radius: 10px")
        self.fr_inside.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_inside.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_inside.setObjectName("fr_inside")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.fr_inside)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.fr_inside)
        self.frame_4.setMaximumSize(QtCore.QSize(600, 16777215))
        self.frame_4.setStyleSheet("border-width: 0;\n"
"background: transparent")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setMaximumSize(QtCore.QSize(160, 25))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 75 12pt \"Georgia\";\n"
"background-color: rgba(0, 0, 0,.9);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding-left: 5px")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.fr_inside)
        self.frame_5.setMaximumSize(QtCore.QSize(600, 16777215))
        self.frame_5.setStyleSheet("border-width: 0;\n"
"background: transparent")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setMaximumSize(QtCore.QSize(105, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(0, 0, 0,.7);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding:2px")
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.ln_nome = QtWidgets.QLineEdit(self.frame_5)
        self.ln_nome.setMaximumSize(QtCore.QSize(450, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ln_nome.setFont(font)
        self.ln_nome.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-width: 1px;\n"
"border-color: black;\n"
"border-radius: 5px;\n"
"padding-left: 10px")
        self.ln_nome.setObjectName("ln_nome")
        self.gridLayout_3.addWidget(self.ln_nome, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.fr_inside)
        self.frame_6.setMaximumSize(QtCore.QSize(600, 16777215))
        self.frame_6.setStyleSheet("border-width: 0;\n"
"background: transparent")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        self.label_4.setMaximumSize(QtCore.QSize(105, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgba(0, 0, 0,.7);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding:2px")
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.ln_cargo = QtWidgets.QLineEdit(self.frame_6)
        self.ln_cargo.setMaximumSize(QtCore.QSize(450, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ln_cargo.setFont(font)
        self.ln_cargo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-width: 1px;\n"
"border-color: black;\n"
"border-radius: 5px;\n"
"padding-left: 10px")
        self.ln_cargo.setObjectName("ln_cargo")
        self.gridLayout_4.addWidget(self.ln_cargo, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.fr_inside)
        self.frame_7.setMaximumSize(QtCore.QSize(600, 16777215))
        self.frame_7.setStyleSheet("border-width: 0;\n"
"background: transparent")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.ln_funcao = QtWidgets.QLineEdit(self.frame_7)
        self.ln_funcao.setMaximumSize(QtCore.QSize(450, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ln_funcao.setFont(font)
        self.ln_funcao.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-width: 1px;\n"
"border-color: black;\n"
"border-radius: 5px;\n"
"padding-left: 10px")
        self.ln_funcao.setObjectName("ln_funcao")
        self.gridLayout_5.addWidget(self.ln_funcao, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_7)
        self.label_5.setMaximumSize(QtCore.QSize(105, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgba(0, 0, 0,.7);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding:2px")
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.fr_inside)
        self.frame_8.setMaximumSize(QtCore.QSize(600, 16777215))
        self.frame_8.setStyleSheet("border-width: 0;\n"
"background: transparent")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_6 = QtWidgets.QLabel(self.frame_8)
        self.label_6.setMaximumSize(QtCore.QSize(105, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgba(0, 0, 0,.7);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding:2px")
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 0, 0, 1, 1)
        self.ln_horario = QtWidgets.QLineEdit(self.frame_8)
        self.ln_horario.setMaximumSize(QtCore.QSize(450, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ln_horario.setFont(font)
        self.ln_horario.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-width: 1px;\n"
"border-color: black;\n"
"border-radius: 5px;\n"
"padding-left: 10px")
        self.ln_horario.setObjectName("ln_horario")
        self.gridLayout_6.addWidget(self.ln_horario, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.fr_inside)
        self.frame_9.setMaximumSize(QtCore.QSize(600, 16777215))
        self.frame_9.setStyleSheet("border-width: 0;\n"
"background: transparent")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_7 = QtWidgets.QLabel(self.frame_9)
        self.label_7.setMaximumSize(QtCore.QSize(105, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgba(0, 0, 0,.7);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding:2px")
        self.label_7.setObjectName("label_7")
        self.gridLayout_7.addWidget(self.label_7, 0, 0, 1, 1)
        self.ln_admissao = QtWidgets.QLineEdit(self.frame_9)
        self.ln_admissao.setMaximumSize(QtCore.QSize(450, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ln_admissao.setFont(font)
        self.ln_admissao.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-width: 1px;\n"
"border-color: black;\n"
"border-radius: 5px;\n"
"padding-left: 10px")
        self.ln_admissao.setObjectName("ln_admissao")
        self.gridLayout_7.addWidget(self.ln_admissao, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.fr_inside)
        self.frame_10.setMaximumSize(QtCore.QSize(600, 16777215))
        self.frame_10.setStyleSheet("border-width: 0;\n"
"background: transparent")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.bt_cadastrar = QtWidgets.QPushButton(self.frame_10)
        self.bt_cadastrar.setMaximumSize(QtCore.QSize(120, 50))
        self.bt_cadastrar.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,.7);\n"
"    color: rgb(0, 0, 0);\n"
"    font: 75 12pt \"Arial\";\n"
"    border-width: 1px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    border-radius: 10px\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 12pt \"Arial\";\n"
"}")
        self.bt_cadastrar.setIconSize(QtCore.QSize(16, 16))
        self.bt_cadastrar.setObjectName("bt_cadastrar")
        self.gridLayout_10.addWidget(self.bt_cadastrar, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_10)
        self.horizontalLayout_3.addWidget(self.fr_inside)
        self.fr_inside_2 = QtWidgets.QFrame(self.frame_2)
        self.fr_inside_2.setMaximumSize(QtCore.QSize(620, 16777215))
        self.fr_inside_2.setStyleSheet("")
        self.fr_inside_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_inside_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_inside_2.setObjectName("fr_inside_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.fr_inside_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.bt_exit = QtWidgets.QPushButton(self.fr_inside_2)
        self.bt_exit.setMaximumSize(QtCore.QSize(130, 16777215))
        self.bt_exit.setStyleSheet("QPushButton{\n"
"    background: transparent;\n"
"    background-color: rgb(0, 0, 0);\n"
"    font: 75 12pt \"Arial\";\n"
"    color: rgb(255, 255, 255);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: white;\n"
"    border-radius: 5px;\n"
"    padding: 5px\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.bt_exit.setObjectName("bt_exit")
        self.gridLayout_8.addWidget(self.bt_exit, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.fr_inside_2)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.fr_low)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sistema de Avaliação do Profissional - SisAvalPro - Tela PRINCIPAL"))
        item = self.tabela_colab.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tabela_colab.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NOME"))
        item = self.tabela_colab.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "CARGO"))
        item = self.tabela_colab.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "FUNÇÃO"))
        item = self.tabela_colab.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "HORÁRIO"))
        item = self.tabela_colab.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "ADMISSÃO"))
        self.bt_avaliar.setText(_translate("MainWindow", "AVALIAR"))
        self.bt_editar.setText(_translate("MainWindow", "EDITAR"))
        self.bt_excluir.setText(_translate("MainWindow", "EXCLUIR"))
        self.label.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">NOVO CADASTRO</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "NOME :"))
        self.label_4.setText(_translate("MainWindow", "CARGO :"))
        self.label_5.setText(_translate("MainWindow", "FUNÇÃO :"))
        self.label_6.setText(_translate("MainWindow", "HORÁRIO :"))
        self.label_7.setText(_translate("MainWindow", "ADMISSÃO :"))
        self.bt_cadastrar.setText(_translate("MainWindow", "CADASTRAR"))
        self.bt_exit.setText(_translate("MainWindow", "Sair do Sistema"))

# Utilizar em caso de teste

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Principal()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())
