from PyQt5 import QtCore, QtGui, QtWidgets
import Back_Login

class Ui_Login(object):
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
        self.frame.setStyleSheet("background-image: url(:/img/Back_Login.png);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: white")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(350, 200))
        self.frame_2.setStyleSheet("background: transparent;\n"
"background-color: rgba(0,0,0,0.3);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: white;\n"
"border-radius: 10px")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setStyleSheet("background: transparent;\n"
"border-width: 0")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setMaximumSize(QtCore.QSize(33, 33))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./icons/userwoman.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.ln_login = QtWidgets.QLineEdit(self.frame_3)
        self.ln_login.setMaximumSize(QtCore.QSize(250, 33))
        self.ln_login.setStyleSheet("border-width: 1px;\n"
"border-color:black;\n"
"color: rgb(0, 0, 0);\n"
"font: 75 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"padding-left: 6px")
        self.ln_login.setObjectName("ln_login")
        self.horizontalLayout_2.addWidget(self.ln_login)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setStyleSheet("background: transparent;\n"
"border-width: 0")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setMaximumSize(QtCore.QSize(33, 33))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("./icons/password.png"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.ln_senha = QtWidgets.QLineEdit(self.frame_4)
        self.ln_senha.setMaximumSize(QtCore.QSize(250, 33))
        self.ln_senha.setStyleSheet("border-width: 1px;\n"
"border-color:black;\n"
"color: rgb(0, 0, 0);\n"
"font: 75 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"padding-left: 6px")
        self.ln_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ln_senha.setObjectName("ln_senha")
        self.horizontalLayout.addWidget(self.ln_senha)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setStyleSheet("background: transparent;\n"
"border-width: 0")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.bt_entrar = QtWidgets.QPushButton(self.frame_5)
        self.bt_entrar.setMaximumSize(QtCore.QSize(80, 40))
        self.bt_entrar.setStyleSheet("QPushButton{\n"
"    font: 75 12pt \"Arial\";\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 1px;\n"
"    border-color: black\n"
"}\n"
"QPushButton:pressed{\n"
"    font: 75 12pt \"Arial\";\n"
"    background-color: rgb(0, 0, 0);\n"
"    border-radius: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"    border-color: white\n"
"}")
        self.bt_entrar.setObjectName("bt_entrar")
        self.gridLayout_2.addWidget(self.bt_entrar, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_5)
        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sistema de Avaliação do Profissional - SisAvalPro - Tela de LOGIN"))
        self.ln_login.setPlaceholderText(_translate("MainWindow", "Digite seu login..."))
        self.ln_senha.setPlaceholderText(_translate("MainWindow", "Digite sua senha..."))
        self.bt_entrar.setText(_translate("MainWindow", "ENTRAR"))

# Utilizar em caso de teste

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())