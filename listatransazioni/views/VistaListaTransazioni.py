from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QSizePolicy

from listatransazioni.controller.ControllerListaTransazioni import ControllerListaTransazioni
from listatransazioni.views.VistaInserisciTransazione import VistaInserisciTransazione
from transazione.views.VistaTransazione import VistaTransazione


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
        buttons_layout.addWidget(self.get_generic_button("Nuova", self.show_new_transazione))

        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(720, 400)
        self.setWindowTitle("Lista Transazioni")

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def show_selected_info(self):
        if len(self.list_view.selectedIndexes()) > 0:
            selected = self.list_view.selectedIndexes()[0].row()
            transazione_selezionata = self.controller.get_transazione_by_index(selected)
            self.vista_transazione = VistaTransazione(transazione_selezionata)
            self.vista_transazione.show()

    def show_new_transazione(self):
        self.vista_inserisci_transazione = VistaInserisciTransazione(self.controller, self.update_ui)
        self.vista_inserisci_transazione.show()

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for transazione in self.controller.get_lista_transazioni():
            item = QStandardItem()
            item.setText(transazione.get_oggetto_venduto().nome + " " + str(transazione.get_oggetto_venduto().prezzo) + " € "
                + transazione.get_data_vendita().strftime("%d-%m-%Y") + "\n"
                + "Acquirente: " + transazione.get_acquirente().nome + " " + transazione.get_acquirente().cognome + " ")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(12)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def closeEvent(self, event):
        self.controller.save_data()