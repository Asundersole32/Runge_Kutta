from view.screen import Ui_Runge_Kutta
from PyQt5 import QtWidgets
import sys


app = QtWidgets.QApplication(sys.argv)
Principal = QtWidgets.QMainWindow()
ui = Ui_Runge_Kutta()
ui.setupUi(Principal)
Principal.show()
sys.exit(app.exec_())