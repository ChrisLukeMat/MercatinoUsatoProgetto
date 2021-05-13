import os
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
from home.views.VistaHome import VistaHome

cod_dipendente = 0
cod_oggetto = 0

if __name__ == '__main__':
    app = QApplication(sys.argv)

    qss = "appStyle/Darkeum.qss"
    with open(qss, "r") as fh:
        app.setStyleSheet(fh.read())

    app.setWindowIcon(QtGui.QIcon("appStyle/IconaMarket.png"))
    vista_home = VistaHome()
    vista_home.show()
    sys.exit(app.exec_())