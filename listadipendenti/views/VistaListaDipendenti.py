from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QSizePolicy, QMessageBox

from dipendente.views.VistaInserisciDipendente import VistaInserisciDipendente
from listadipendenti.controller.ControllerListaDipendenti import ControllerListaDipendenti
from dipendente.views.VistaDipendente import VistaDipendente


class VistaListaDipendenti(QWidget):
    def __init__(self, parent=None):
        super(VistaListaDipendenti, self).__init__(parent)

        h_layout = QHBoxLayout()
        self.controller = ControllerListaDipendenti()
        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(self.get_generic_button("Apri", self.show_selected_info))
        buttons_layout.addWidget(self.get_generic_button("Nuovo", self.show_new_dipendente))
        buttons_layout.addWidget(self.get_generic_button("Elimina", self.show_elimina_dipendente))

        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600, 300)
        self.setWindowTitle("Lista dipendenti")

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def show_selected_info(self):
        selected = self.list_view.selectedIndexes()[0].row()
        dipendente_selezionato = self.controller.get_dipendente_by_index(selected)
        self.vista_dipendente = VistaDipendente(dipendente_selezionato)#, self.controller.rimuovi_dipendente_by_id, self.update_ui)
        self.vista_dipendente.show()

    def show_new_dipendente(self):
        self.vista_inserisci_dipendente = VistaInserisciDipendente(self.controller, self.update_ui)
        self.vista_inserisci_dipendente.show()

    def show_modifica_dipendente(self):
        # self.vista_modifica_dipendente = VistaModificaDipendente()
        pass

    def show_elimina_dipendente(self):
        selected = self.list_view.selectedIndexes()[0].row()
        dipendente_selezionato = self.controller.get_dipendente_by_index(selected)
        self.controller.rimuovi_dipendente_by_id(dipendente_selezionato.get_id)
        QMessageBox.Ok("Il dipendente: {} {} e' stato eliminato".format(dipendente_selezionato.get_nome, dipendente_selezionato.get_cognome))

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for dipendente in self.controller.get_lista_dipendenti():
            i = 1
            item = QStandardItem()
            item.setText(i + ") " + dipendente.nome + " | " + dipendente.cognome)
            item.setEditable(False)
            font = item.font()
            font.setFontSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
            i = int(i) + 1
        self.list_view.setModel(self.listview_model)

    def closeEvent(self, event):
        self.controller.save_data()