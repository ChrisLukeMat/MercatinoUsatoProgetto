from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QSizePolicy

from catalogo.controller.ControllerCatalogo import ControllerCatalogo
from catalogo.views import VistaInserisciOggetto
from oggetto.views.VistaOggetto import VistaOggetto


class VistaCatalogo(QWidget):
    def __init__(self, parent=None):
        super(VistaCatalogo, self).__init__(parent)

        h_layout = QHBoxLayout()
        self.controller = ControllerCatalogo()
        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(self.get_generic_button("Apri",self.show_selected_info))
        buttons_layout.addWidget(self.get_generic_button("Nuovo",self.show_new_oggetto))
        buttons_layout.addWidget(self.get_generic_button("Modifica", self.show_modifica_oggetto))

        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600,300)
        self.setWindowTitle("Catalogo")

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def show_selected_info(self):
        selected = self.list_view.selectedIndexes()[0].row()
        oggetto_selezionato = self.controller.get_oggetto_by_index(selected)
        self.vista_oggetto = VistaOggetto(oggetto_selezionato, self.controller.rimuovi_oggetto_by_id, self.update_ui)
        self.vista_oggetto.show()

    def show_new_oggetto(self):
        self.vista_inserisci_oggetto = VistaInserisciOggetto(self.controller,self.update_ui)
        self.vista_inserisci_oggetto.show()

    def show_modifica_oggetto(self):
       # self.vista_modifica_oggetto = VistaModificaOggetto()
       pass

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for oggetto in self.controller.get_catalogo():
            i = 1
            item = QStandardItem()
            item.setText(i + ") " + oggetto.nome + " | " + oggetto.prezzo)
            item.setEditable(False)
            font = item.font()
            font.setFontSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
            i = int(i) + 1
        self.list_view.setModel(self.listview_model)

    def closeEvent(self, event):
        self.controller.save_data()