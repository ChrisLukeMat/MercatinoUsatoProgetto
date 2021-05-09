from PyQt5.QtWidgets import QWidget

from oggetto.controller.ControllerOggetto import ControllerOggetto


class VistaOggetto(QWidget):
    def __init__(self, oggetto, parent=None):
        super(VistaOggetto, self).__init__()
        self.controller = ControllerOggetto(oggetto)
