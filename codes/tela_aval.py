from PyQt5 import QtCore, QtGui, QtWidgets
import Back_Aval

class Ui_Aval(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(815, 638)
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
        self.frame.setStyleSheet("background-image: url(:/img/Back_Aval.png);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fr_high = QtWidgets.QFrame(self.frame)
        self.fr_high.setMaximumSize(QtCore.QSize(16777215, 450))
        self.fr_high.setStyleSheet("background:transparent;\n"
"border-width:0")
        self.fr_high.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_high.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_high.setObjectName("fr_high")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.fr_high)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_5 = QtWidgets.QWidget(self.fr_high)
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 400))
        self.widget_5.setStyleSheet("")
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_12 = QtWidgets.QLabel(self.widget_5)
        self.label_12.setMaximumSize(QtCore.QSize(80, 37))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgba(0, 0, 0,.5);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding:2px")
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 1, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.widget_5)
        self.label_14.setMaximumSize(QtCore.QSize(80, 37))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: rgba(0, 0, 0,.5);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding:2px")
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 4, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.widget_5)
        self.label_16.setMaximumSize(QtCore.QSize(80, 37))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color: rgba(0, 0, 0,.5);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding:2px")
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 6, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.widget_5)
        self.label_17.setMaximumSize(QtCore.QSize(80, 37))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("background-color: rgba(0, 0, 0,.5);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding:2px")
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 7, 0, 1, 1)
        self.lb_tecnol = QtWidgets.QLabel(self.widget_5)
        self.lb_tecnol.setMaximumSize(QtCore.QSize(37, 37))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tecnol.setFont(font)
        self.lb_tecnol.setStyleSheet("")
        self.lb_tecnol.setText("")
        self.lb_tecnol.setObjectName("lb_tecnol")
        self.gridLayout_3.addWidget(self.lb_tecnol, 6, 1, 1, 2)
        self.lb_proativi = QtWidgets.QLabel(self.widget_5)
        self.lb_proativi.setMaximumSize(QtCore.QSize(37, 37))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_proativi.setFont(font)
        self.lb_proativi.setStyleSheet("")
        self.lb_proativi.setText("")
        self.lb_proativi.setObjectName("lb_proativi")
        self.gridLayout_3.addWidget(self.lb_proativi, 4, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.widget_5)
        self.label_11.setMaximumSize(QtCore.QSize(80, 37))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgba(0, 0, 0,.5);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding:2px")
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 1)
        self.lb_dina = QtWidgets.QLabel(self.widget_5)
        self.lb_dina.setMaximumSize(QtCore.QSize(37, 37))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_dina.setFont(font)
        self.lb_dina.setStyleSheet("")
        self.lb_dina.setText("")
        self.lb_dina.setObjectName("lb_dina")
        self.gridLayout_3.addWidget(self.lb_dina, 5, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.widget_5)
        self.label_13.setMaximumSize(QtCore.QSize(80, 37))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgba(0, 0, 0,.5);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding:2px")
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 3, 0, 1, 1)
        self.lb_assidu = QtWidgets.QLabel(self.widget_5)
        self.lb_assidu.setMaximumSize(QtCore.QSize(37, 37))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_assidu.setFont(font)
        self.lb_assidu.setStyleSheet("")
        self.lb_assidu.setText("")
        self.lb_assidu.setObjectName("lb_assidu")
        self.gridLayout_3.addWidget(self.lb_assidu, 7, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.widget_5)
        self.label_15.setMaximumSize(QtCore.QSize(80, 37))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: rgba(0, 0, 0,.5);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding:2px")
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 5, 0, 1, 1)
        self.lb_expe = QtWidgets.QLabel(self.widget_5)
        self.lb_expe.setMaximumSize(QtCore.QSize(37, 37))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_expe.setFont(font)
        self.lb_expe.setStyleSheet("")
        self.lb_expe.setText("")
        self.lb_expe.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_expe.setObjectName("lb_expe")
        self.gridLayout_3.addWidget(self.lb_expe, 1, 1, 1, 1)
        self.lb_atendi = QtWidgets.QLabel(self.widget_5)
        self.lb_atendi.setMaximumSize(QtCore.QSize(37, 37))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_atendi.setFont(font)
        self.lb_atendi.setStyleSheet("")
        self.lb_atendi.setText("")
        self.lb_atendi.setObjectName("lb_atendi")
        self.gridLayout_3.addWidget(self.lb_atendi, 3, 1, 1, 1)
        self.lb_pontu = QtWidgets.QLabel(self.widget_5)
        self.lb_pontu.setMaximumSize(QtCore.QSize(37, 37))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_pontu.setFont(font)
        self.lb_pontu.setStyleSheet("")
        self.lb_pontu.setText("")
        self.lb_pontu.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_pontu.setObjectName("lb_pontu")
        self.gridLayout_3.addWidget(self.lb_pontu, 0, 1, 1, 3)
        self.gridLayout_2.addWidget(self.widget_5, 1, 1, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.fr_high)
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_3.setStyleSheet("background-color: rgba(0, 0, 0,0.2);")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setMaximumSize(QtCore.QSize(200, 35))
        self.label_2.setStyleSheet("font: 75 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"padding: 5px")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lb_nomeColab = QtWidgets.QLabel(self.widget_3)
        self.lb_nomeColab.setMaximumSize(QtCore.QSize(600, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_nomeColab.setFont(font)
        self.lb_nomeColab.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color: black;\n"
"border-radius: 5px;\n"
"padding-left: 10px")
        self.lb_nomeColab.setText("")
        self.lb_nomeColab.setObjectName("lb_nomeColab")
        self.horizontalLayout.addWidget(self.lb_nomeColab)
        spacerItem = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_2.addWidget(self.widget_3, 0, 0, 1, 2)
        self.widget_4 = QtWidgets.QWidget(self.fr_high)
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 400))
        self.widget_4.setStyleSheet("")
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.expe_triste = QtWidgets.QToolButton(self.widget_4)
        self.expe_triste.setMaximumSize(QtCore.QSize(37, 37))
        self.expe_triste.setStyleSheet("")
        self.expe_triste.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/triste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.expe_triste.setIcon(icon)
        self.expe_triste.setIconSize(QtCore.QSize(40, 21))
        self.expe_triste.setObjectName("expe_triste")
        self.gridLayout_4.addWidget(self.expe_triste, 1, 1, 1, 1)
        self.assidu_feliz = QtWidgets.QToolButton(self.widget_4)
        self.assidu_feliz.setMaximumSize(QtCore.QSize(37, 37))
        self.assidu_feliz.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./icons/feliz.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.assidu_feliz.setIcon(icon1)
        self.assidu_feliz.setIconSize(QtCore.QSize(40, 22))
        self.assidu_feliz.setObjectName("assidu_feliz")
        self.gridLayout_4.addWidget(self.assidu_feliz, 6, 3, 1, 1)
        self.proativi_feliz = QtWidgets.QToolButton(self.widget_4)
        self.proativi_feliz.setMaximumSize(QtCore.QSize(37, 37))
        self.proativi_feliz.setText("")
        self.proativi_feliz.setIcon(icon1)
        self.proativi_feliz.setIconSize(QtCore.QSize(40, 22))
        self.proativi_feliz.setObjectName("proativi_feliz")
        self.gridLayout_4.addWidget(self.proativi_feliz, 3, 3, 1, 1)
        self.expe_feliz = QtWidgets.QToolButton(self.widget_4)
        self.expe_feliz.setMaximumSize(QtCore.QSize(37, 37))
        self.expe_feliz.setText("")
        self.expe_feliz.setIcon(icon1)
        self.expe_feliz.setIconSize(QtCore.QSize(40, 22))
        self.expe_feliz.setObjectName("expe_feliz")
        self.gridLayout_4.addWidget(self.expe_feliz, 1, 3, 1, 1)
        self.tecnol_triste = QtWidgets.QToolButton(self.widget_4)
        self.tecnol_triste.setMaximumSize(QtCore.QSize(37, 37))
        self.tecnol_triste.setStyleSheet("")
        self.tecnol_triste.setText("")
        self.tecnol_triste.setIcon(icon)
        self.tecnol_triste.setIconSize(QtCore.QSize(40, 21))
        self.tecnol_triste.setObjectName("tecnol_triste")
        self.gridLayout_4.addWidget(self.tecnol_triste, 5, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget_4)
        self.label_8.setMaximumSize(QtCore.QSize(120, 37))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgba(0, 0, 0,.5);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding:2px")
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 4, 0, 1, 1)
        self.pontu_neutro = QtWidgets.QToolButton(self.widget_4)
        self.pontu_neutro.setMaximumSize(QtCore.QSize(37, 37))
        self.pontu_neutro.setStyleSheet("")
        self.pontu_neutro.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./icons/neutro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pontu_neutro.setIcon(icon2)
        self.pontu_neutro.setIconSize(QtCore.QSize(40, 23))
        self.pontu_neutro.setObjectName("pontu_neutro")
        self.gridLayout_4.addWidget(self.pontu_neutro, 0, 2, 1, 1)
        self.tecnol_neutro = QtWidgets.QToolButton(self.widget_4)
        self.tecnol_neutro.setMaximumSize(QtCore.QSize(37, 37))
        self.tecnol_neutro.setStyleSheet("")
        self.tecnol_neutro.setText("")
        self.tecnol_neutro.setIcon(icon2)
        self.tecnol_neutro.setIconSize(QtCore.QSize(40, 23))
        self.tecnol_neutro.setObjectName("tecnol_neutro")
        self.gridLayout_4.addWidget(self.tecnol_neutro, 5, 2, 1, 1)
        self.proativi_triste = QtWidgets.QToolButton(self.widget_4)
        self.proativi_triste.setMaximumSize(QtCore.QSize(37, 37))
        self.proativi_triste.setStyleSheet("")
        self.proativi_triste.setText("")
        self.proativi_triste.setIcon(icon)
        self.proativi_triste.setIconSize(QtCore.QSize(40, 21))
        self.proativi_triste.setObjectName("proativi_triste")
        self.gridLayout_4.addWidget(self.proativi_triste, 3, 1, 1, 1)
        self.atendi_triste = QtWidgets.QToolButton(self.widget_4)
        self.atendi_triste.setMaximumSize(QtCore.QSize(37, 37))
        self.atendi_triste.setStyleSheet("")
        self.atendi_triste.setText("")
        self.atendi_triste.setIcon(icon)
        self.atendi_triste.setIconSize(QtCore.QSize(40, 21))
        self.atendi_triste.setObjectName("atendi_triste")
        self.gridLayout_4.addWidget(self.atendi_triste, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget_4)
        self.label_5.setMaximumSize(QtCore.QSize(120, 37))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgba(0, 0, 0,.5);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding:2px")
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 1, 0, 1, 1)
        self.dina_neutro = QtWidgets.QToolButton(self.widget_4)
        self.dina_neutro.setMaximumSize(QtCore.QSize(37, 37))
        self.dina_neutro.setStyleSheet("")
        self.dina_neutro.setText("")
        self.dina_neutro.setIcon(icon2)
        self.dina_neutro.setIconSize(QtCore.QSize(40, 23))
        self.dina_neutro.setObjectName("dina_neutro")
        self.gridLayout_4.addWidget(self.dina_neutro, 4, 2, 1, 1)
        self.proativi_neutro = QtWidgets.QToolButton(self.widget_4)
        self.proativi_neutro.setMaximumSize(QtCore.QSize(37, 37))
        self.proativi_neutro.setStyleSheet("")
        self.proativi_neutro.setText("")
        self.proativi_neutro.setIcon(icon2)
        self.proativi_neutro.setIconSize(QtCore.QSize(40, 23))
        self.proativi_neutro.setObjectName("proativi_neutro")
        self.gridLayout_4.addWidget(self.proativi_neutro, 3, 2, 1, 1)
        self.atendi_feliz = QtWidgets.QToolButton(self.widget_4)
        self.atendi_feliz.setMaximumSize(QtCore.QSize(37, 37))
        self.atendi_feliz.setText("")
        self.atendi_feliz.setIcon(icon1)
        self.atendi_feliz.setIconSize(QtCore.QSize(40, 22))
        self.atendi_feliz.setObjectName("atendi_feliz")
        self.gridLayout_4.addWidget(self.atendi_feliz, 2, 3, 1, 1)
        self.dina_feliz = QtWidgets.QToolButton(self.widget_4)
        self.dina_feliz.setMaximumSize(QtCore.QSize(37, 37))
        self.dina_feliz.setText("")
        self.dina_feliz.setIcon(icon1)
        self.dina_feliz.setIconSize(QtCore.QSize(40, 22))
        self.dina_feliz.setObjectName("dina_feliz")
        self.gridLayout_4.addWidget(self.dina_feliz, 4, 3, 1, 1)
        self.assidu_neutro = QtWidgets.QToolButton(self.widget_4)
        self.assidu_neutro.setMaximumSize(QtCore.QSize(37, 37))
        self.assidu_neutro.setStyleSheet("")
        self.assidu_neutro.setText("")
        self.assidu_neutro.setIcon(icon2)
        self.assidu_neutro.setIconSize(QtCore.QSize(40, 23))
        self.assidu_neutro.setObjectName("assidu_neutro")
        self.gridLayout_4.addWidget(self.assidu_neutro, 6, 2, 1, 1)
        self.atendi_neutro = QtWidgets.QToolButton(self.widget_4)
        self.atendi_neutro.setMaximumSize(QtCore.QSize(37, 37))
        self.atendi_neutro.setStyleSheet("")
        self.atendi_neutro.setText("")
        self.atendi_neutro.setIcon(icon2)
        self.atendi_neutro.setIconSize(QtCore.QSize(40, 23))
        self.atendi_neutro.setObjectName("atendi_neutro")
        self.gridLayout_4.addWidget(self.atendi_neutro, 2, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget_4)
        self.label_10.setMaximumSize(QtCore.QSize(120, 37))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgba(0, 0, 0,.5);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding:2px")
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 6, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget_4)
        self.label_9.setMaximumSize(QtCore.QSize(120, 37))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgba(0, 0, 0,.5);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding:2px")
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 5, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget_4)
        self.label_6.setMaximumSize(QtCore.QSize(120, 37))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgba(0, 0, 0,.5);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding:2px")
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 2, 0, 1, 1)
        self.assidu_triste = QtWidgets.QToolButton(self.widget_4)
        self.assidu_triste.setMaximumSize(QtCore.QSize(37, 37))
        self.assidu_triste.setStyleSheet("")
        self.assidu_triste.setText("")
        self.assidu_triste.setIcon(icon)
        self.assidu_triste.setIconSize(QtCore.QSize(40, 21))
        self.assidu_triste.setObjectName("assidu_triste")
        self.gridLayout_4.addWidget(self.assidu_triste, 6, 1, 1, 1)
        self.tecnol_feliz = QtWidgets.QToolButton(self.widget_4)
        self.tecnol_feliz.setMaximumSize(QtCore.QSize(37, 37))
        self.tecnol_feliz.setText("")
        self.tecnol_feliz.setIcon(icon1)
        self.tecnol_feliz.setIconSize(QtCore.QSize(40, 22))
        self.tecnol_feliz.setObjectName("tecnol_feliz")
        self.gridLayout_4.addWidget(self.tecnol_feliz, 5, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget_4)
        self.label_7.setMaximumSize(QtCore.QSize(120, 37))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgba(0, 0, 0,.5);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding:2px")
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 3, 0, 1, 1)
        self.dina_triste = QtWidgets.QToolButton(self.widget_4)
        self.dina_triste.setMaximumSize(QtCore.QSize(37, 37))
        self.dina_triste.setStyleSheet("")
        self.dina_triste.setText("")
        self.dina_triste.setIcon(icon)
        self.dina_triste.setIconSize(QtCore.QSize(40, 21))
        self.dina_triste.setObjectName("dina_triste")
        self.gridLayout_4.addWidget(self.dina_triste, 4, 1, 1, 1)
        self.pontu_triste = QtWidgets.QToolButton(self.widget_4)
        self.pontu_triste.setMaximumSize(QtCore.QSize(37, 37))
        self.pontu_triste.setStyleSheet("")
        self.pontu_triste.setText("")
        self.pontu_triste.setIcon(icon)
        self.pontu_triste.setIconSize(QtCore.QSize(40, 21))
        self.pontu_triste.setObjectName("pontu_triste")
        self.gridLayout_4.addWidget(self.pontu_triste, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setMaximumSize(QtCore.QSize(120, 37))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgba(0, 0, 0,.5);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding:2px")
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.expe_neutro = QtWidgets.QToolButton(self.widget_4)
        self.expe_neutro.setMaximumSize(QtCore.QSize(37, 37))
        self.expe_neutro.setStyleSheet("")
        self.expe_neutro.setText("")
        self.expe_neutro.setIcon(icon2)
        self.expe_neutro.setIconSize(QtCore.QSize(40, 23))
        self.expe_neutro.setObjectName("expe_neutro")
        self.gridLayout_4.addWidget(self.expe_neutro, 1, 2, 1, 1)
        self.pontu_feliz = QtWidgets.QToolButton(self.widget_4)
        self.pontu_feliz.setMaximumSize(QtCore.QSize(37, 37))
        self.pontu_feliz.setStyleSheet("")
        self.pontu_feliz.setText("")
        self.pontu_feliz.setIcon(icon1)
        self.pontu_feliz.setIconSize(QtCore.QSize(40, 22))
        self.pontu_feliz.setObjectName("pontu_feliz")
        self.gridLayout_4.addWidget(self.pontu_feliz, 0, 3, 1, 1)
        self.gridLayout_2.addWidget(self.widget_4, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.fr_high)
        self.fr_mid = QtWidgets.QFrame(self.frame)
        self.fr_mid.setMaximumSize(QtCore.QSize(16777215, 50))
        self.fr_mid.setStyleSheet("background: transparent;\n"
"border-width:0")
        self.fr_mid.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_mid.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_mid.setObjectName("fr_mid")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.fr_mid)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label = QtWidgets.QLabel(self.fr_mid)
        self.label.setMaximumSize(QtCore.QSize(350, 30))
        self.label.setStyleSheet("background-color: rgba(0, 0, 0,.5);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px")
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.fr_mid)
        self.fr_low = QtWidgets.QFrame(self.frame)
        self.fr_low.setMaximumSize(QtCore.QSize(16777215, 180))
        self.fr_low.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-radius: 10px;\n"
"background: transparent")
        self.fr_low.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_low.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_low.setObjectName("fr_low")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fr_low)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.fr_low)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget.setStyleSheet("border-width:0")
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rel_supervisor = QtWidgets.QTextEdit(self.widget)
        self.rel_supervisor.setMaximumSize(QtCore.QSize(16777215, 115))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.rel_supervisor.setFont(font)
        self.rel_supervisor.setStyleSheet("border-width: 0;\n"
"background-color: rgba(0,0,0,.7);\n"
"font: 12pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"padding-left: 10px")
        self.rel_supervisor.setObjectName("rel_supervisor")
        self.horizontalLayout_2.addWidget(self.rel_supervisor)
        self.verticalLayout_2.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.fr_low)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_2.setStyleSheet("border-width: 0;")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bt_relatorio = QtWidgets.QPushButton(self.widget_2)
        self.bt_relatorio.setMaximumSize(QtCore.QSize(160, 40))
        self.bt_relatorio.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 75 12pt \"Arial\";\n"
"    border-width: 1px;\n"
"    border-radius: 10px\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 12pt \"Arial\";\n"
"    border-width: 2px;\n"
"    border-color: white;\n"
"    border-radius: 10px\n"
"\n"
"}")
        self.bt_relatorio.setObjectName("bt_relatorio")
        self.horizontalLayout_3.addWidget(self.bt_relatorio)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.fr_low)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sistema de Avaliação do Profissional - SisAvalPro - Tela de AVALIAÇÃO"))
        MainWindow.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">OPÇÃO :</p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">OPÇÃO :</p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">OPÇÃO :</p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">OPÇÃO :</p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">OPÇÃO :</p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">OPÇÃO :</p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">OPÇÃO :</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">NOME DO AVALIADO :</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "DINÂMICA"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>EXPERIÊNCIA</p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "ASSIDUIDADE"))
        self.label_9.setText(_translate("MainWindow", "TECNOLOGIA"))
        self.label_6.setText(_translate("MainWindow", "ATENDIMENTO"))
        self.label_7.setText(_translate("MainWindow", "PROATIVIDADE"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>PONTUALIDADE</p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">CONSIDERAÇÕES FINAIS DA SUPERVISÃO</p></body></html>"))
        self.bt_relatorio.setText(_translate("MainWindow", "GERAR RELATÓRIO"))

# Utilizar em caso de teste

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Aval()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())
