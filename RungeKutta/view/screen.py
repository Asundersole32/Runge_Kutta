from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from runge_kutta import rungeKutta


class Ui_Runge_Kutta(object):
    def setupUi(self, Runge_Kutta):
        Runge_Kutta.setObjectName("Runge_Kutta")
        Runge_Kutta.resize(746, 382)
        self.Runge_Kutta_2 = QtWidgets.QWidget(Runge_Kutta)
        self.Runge_Kutta_2.setObjectName("Runge_Kutta_2")
        self.Result_Button = QtWidgets.QPushButton(self.Runge_Kutta_2)
        self.Result_Button.setGeometry(QtCore.QRect(240, 260, 75, 23))
        self.Result_Button.setObjectName("Result_Button")
        self.Exit_Button = QtWidgets.QPushButton(self.Runge_Kutta_2)
        self.Exit_Button.setGeometry(QtCore.QRect(420, 260, 75, 23))
        self.Exit_Button.setObjectName("Exit_Button")
        self.X0_input = QtWidgets.QLineEdit(self.Runge_Kutta_2)
        self.X0_input.setGeometry(QtCore.QRect(240, 160, 113, 20))
        self.X0_input.setObjectName("X0_input")
        self.Function_input = QtWidgets.QLineEdit(self.Runge_Kutta_2)
        self.Function_input.setGeometry(QtCore.QRect(240, 120, 113, 20))
        self.Function_input.setObjectName("Function_input")
        self.Y0_input = QtWidgets.QLineEdit(self.Runge_Kutta_2)
        self.Y0_input.setGeometry(QtCore.QRect(400, 160, 113, 20))
        self.Y0_input.setObjectName("Y0_input")
        self.H_input = QtWidgets.QLineEdit(self.Runge_Kutta_2)
        self.H_input.setGeometry(QtCore.QRect(400, 120, 113, 20))
        self.H_input.setObjectName("H_input")
        self.X0_text = QtWidgets.QLabel(self.Runge_Kutta_2)
        self.X0_text.setGeometry(QtCore.QRect(220, 160, 71, 21))
        self.X0_text.setObjectName("X0_text")
        self.Function_Text = QtWidgets.QLabel(self.Runge_Kutta_2)
        self.Function_Text.setGeometry(QtCore.QRect(200, 120, 71, 21))
        self.Function_Text.setObjectName("Function_Text")
        self.H_Text = QtWidgets.QLabel(self.Runge_Kutta_2)
        self.H_Text.setGeometry(QtCore.QRect(390, 120, 61, 21))
        self.H_Text.setObjectName("H_Text")
        self.Y0_text = QtWidgets.QLabel(self.Runge_Kutta_2)
        self.Y0_text.setGeometry(QtCore.QRect(380, 160, 61, 16))
        self.Y0_text.setObjectName("Y0_text")
        self.X_Text = QtWidgets.QLabel(self.Runge_Kutta_2)
        self.X_Text.setGeometry(QtCore.QRect(300, 200, 71, 21))
        self.X_Text.setObjectName("X_Text")
        self.X_input = QtWidgets.QLineEdit(self.Runge_Kutta_2)
        self.X_input.setGeometry(QtCore.QRect(310, 200, 113, 20))
        self.X_input.setObjectName("X_input")
        self.Title_text = QtWidgets.QLabel(self.Runge_Kutta_2)
        self.Title_text.setGeometry(QtCore.QRect(236, 40, 271, 71))
        self.Title_text.setObjectName("Title_text")
        Runge_Kutta.setCentralWidget(self.Runge_Kutta_2)

        self.retranslateUi(Runge_Kutta)
        self.Exit_Button.clicked.connect(Runge_Kutta.close)
        QtCore.QMetaObject.connectSlotsByName(Runge_Kutta)

        self.Result_Button.clicked.connect(self.Runge_Kutta_calculation)

    def Runge_Kutta_calculation(self):
        function = self.Function_input.text()
        x0 = float(self.X0_input.text())
        y0 = float(self.Y0_input.text())
        h = float(self.H_input.text())
        x = float(self.X_input.text())
        result = rungeKutta(x0, y0, x, h, function)

        msg = QMessageBox()
        msg.setIcon(msg.Information)
        msg.setWindowTitle("Resultado")
        msg.setText("X em Y: "+str(result[0])+"  Variação N: "+str(result[1]))
        msg.exec_()

    def retranslateUi(self, Runge_Kutta):
        _translate = QtCore.QCoreApplication.translate
        Runge_Kutta.setWindowTitle(_translate("Runge_Kutta", "Runge_Kutta"))
        self.Result_Button.setText(_translate("Runge_Kutta", "Calcular"))
        self.Exit_Button.setText(_translate("Runge_Kutta", "Sair"))
        self.X0_text.setText(_translate("Runge_Kutta", "X0"))
        self.Function_Text.setText(_translate("Runge_Kutta", "Função"))
        self.H_Text.setText(_translate("Runge_Kutta", "h"))
        self.Y0_text.setText(_translate("Runge_Kutta", "Y0"))
        self.X_Text.setText(_translate("Runge_Kutta", "X"))
        self.Title_text.setText(_translate("Runge_Kutta", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Calculadora Runge_Kutta</span></p></body></html>"))