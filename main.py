import sys

from PyQt5.QtWidgets import QApplication
from home.views.VistaHome import VistaHome

cod_dipendente = 0
cod_oggetto = 0

if __name__ == '__main__':
    app = QApplication(sys.argv)
    vista_home = VistaHome()
    vista_home.show()
    sys.exit(app.exec_())