from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout

from listatransazioni.controller.ControllerListaTransazioni import ControllerListaTransazioni


class VistaListaTransazioni(QWidget):
    def __init__(self, parent=None):
        super(VistaListaTransazioni, self).__init__(parent)

        h_layout = QHBoxLayout()
        self.controller = ControllerListaTransazioni()
        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(self.get_generic_button("Apri", self.show_selected_info))
        buttons_layout.addWidget(self.get_generic_button("Nuovo", self.show_new_transazione))
        #buttons_layout.addWidget(self.get_generic_button("Modifica", self.show_modifica_transazione))

        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600, 300)
        self.setWindowTitle("Lista Transazioni")