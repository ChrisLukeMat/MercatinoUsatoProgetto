from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QSizePolicy, QMessageBox

from catalogo.controller.ControllerCatalogo import ControllerCatalogo
from catalogo.views.VistaInserisciOggetto import VistaInserisciOggetto
from catalogo.views.VistaModificaOggetto import VistaModificaOggetto
from oggetto.views.VistaOggetto import VistaOggetto

class VistaCatalogo(QWidget):
    def __init__(self, parent=None):
        super(VistaCatalogo, self).__init__(parent)

        self.controller = ControllerCatalogo()
        self.list_view = QListView()
        self.update_ui()
        self.list_view.setMinimumSize(500, 400)
        h_layout = QHBoxLayout()

        catalogo_layout = QVBoxLayout()
        catalogo_layout.addWidget(self.list_view)

        h_layout.addLayout(catalogo_layout)

        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(self.get_generic_button("Apri", self.show_selected_info))
        buttons_layout.addWidget(self.get_generic_button("Nuovo", self.show_new_oggetto))
        buttons_layout.addWidget(self.get_generic_button("Elimina", self.show_elimina_oggetto))
        buttons_layout.addWidget(self.get_generic_button("Modifica", self.show_modifica_oggetto))

        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(720, 400)
        self.setWindowTitle("Catalogo")

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setFixedWidth(350)
        button.setFixedHeight(100)
        button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        button.setFont(QFont("Calibri", 12, QFont.Bold))
        button.clicked.connect(on_click)
        return button

    def show_selected_info(self):
        if len(self.list_view.selectedIndexes()) > 0:
            selected = self.list_view.selectedIndexes()[0].row()
            oggetto_selezionato = self.controller.get_oggetto_by_index(selected)
            self.vista_oggetto = VistaOggetto(oggetto_selezionato)
            self.vista_oggetto.show()

    def show_new_oggetto(self):
        self.vista_inserisci_oggetto = VistaInserisciOggetto(self.controller, self.update_ui)
        self.vista_inserisci_oggetto.show()

    def show_modifica_oggetto(self):
        if len(self.list_view.selectedIndexes()) > 0:
            selected = self.list_view.selectedIndexes()[0].row()
            oggetto_selezionato = self.controller.get_oggetto_by_index(selected)
            self.vista_modifica_oggetto = VistaModificaOggetto(oggetto_selezionato, self.update_ui)
            self.vista_modifica_oggetto.show()

    def show_elimina_oggetto(self):
        if len(self.list_view.selectedIndexes()) > 0:
            selected = self.list_view.selectedIndexes()[0].row()
            oggetto_selezionato = self.controller.get_oggetto_by_index(selected)
            self.controller.rimuovi_oggetto_by_id(oggetto_selezionato.id)
            self.update_ui()
            QMessageBox.critical(self, 'Eliminato', "L' oggetto: {} e' stato eliminato".format(oggetto_selezionato.nome), QMessageBox.Ok,
                                 QMessageBox.Ok)

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        i = 1
        for oggetto in self.controller.get_catalogo():
            item = QStandardItem()
            item.setText(oggetto.nome + " " + str(oggetto.prezzo) + " €")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(12)
            item.setFont(font)
            i = int(i) + 1
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def closeEvent(self, event):
        self.controller.save_data()