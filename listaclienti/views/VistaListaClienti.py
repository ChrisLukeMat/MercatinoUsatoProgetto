from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QSizePolicy, QMessageBox

from cliente.views.VistaInserisciCliente import VistaInserisciCliente
from listaclienti.controller.ControllerListaClienti import ControllerListaClienti
from cliente.views.VistaCliente import VistaCliente


class VistaListaClienti(QWidget):
    def __init__(self, parent=None):
        super(VistaListaClienti, self).__init__(parent)

        h_layout = QHBoxLayout()
        self.controller = ControllerListaClienti()
        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(self.get_generic_button("Apri", self.show_selected_info))
        buttons_layout.addWidget(self.get_generic_button("Nuovo", self.show_new_cliente))
        buttons_layout.addWidget(self.get_generic_button("Elimina", self.show_elimina_cliente))

        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600, 300)
        self.setWindowTitle("Lista clienti")

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def show_selected_info(self):
        selected = self.list_view.selectedIndexes()[0].row()
        cliente_selezionato = self.controller.get_cliente_by_index(selected)
        self.vista_cliente = VistaCliente(cliente_selezionato)#, self.controller.rimuovi_cliente_by_id, self.update_ui)
        self.vista_cliente.show()

    def show_new_cliente(self):
        self.vista_inserisci_cliente = VistaInserisciCliente(self.controller, self.update_ui)
        self.vista_inserisci_cliente.show()

    def show_modifica_cliente(self):
        # self.vista_modifica_cliente = VistaModificaCliente()
        pass

    def show_elimina_cliente(self):
        selected = self.list_view.selectedIndexes()[0].row()
        cliente_selezionato = self.controller.get_cliente_by_index(selected)
        self.controller.rimuovi_cliente_by_id(cliente_selezionato.get_id)
        QMessageBox.Ok("Il cliente: {} {} e' stato eliminato".format(cliente_selezionato.get_nome, cliente_selezionato.get_cognome))

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for cliente in self.controller.get_lista_clienti():
            i = 1
            item = QStandardItem()
            item.setText(str(i) + ") " + cliente.nome + " | " + cliente.cognome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
            i = int(i) + 1
        self.list_view.setModel(self.listview_model)

    def closeEvent(self, event):
        self.controller.save_data()