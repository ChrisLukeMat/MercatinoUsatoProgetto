from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QSizePolicy, QMessageBox

from listaclienti.views.VistaInserisciCliente import VistaInserisciCliente
from listaclienti.controller.ControllerListaClienti import ControllerListaClienti
from cliente.views.VistaCliente import VistaCliente
from listaclienti.views.VistaModificaCliente import VistaModificaCliente


class VistaListaClienti(QWidget):
    def __init__(self, parent=None):
        super(VistaListaClienti, self).__init__(parent)

        self.controller = ControllerListaClienti()
        self.list_view = QListView()
        self.update_ui()
        self.list_view.setMinimumSize(500, 400)
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(self.get_generic_button("Apri", self.show_selected_info))
        buttons_layout.addWidget(self.get_generic_button("Nuovo", self.show_new_cliente))
        buttons_layout.addWidget(self.get_generic_button("Elimina", self.show_elimina_cliente))
        buttons_layout.addWidget(self.get_generic_button("Modifica", self.show_modifica_cliente))

        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(720, 400)
        self.setWindowTitle("Lista clienti")

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setFixedWidth(350)
        button.setFixedHeight(100)
        button.setFont(QFont("Calibri", 12, QFont.Bold))
        button.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        button.clicked.connect(on_click)
        return button

    def show_selected_info(self):
        if len(self.list_view.selectedIndexes()) > 0:
            selected = self.list_view.selectedIndexes()[0].row()
            cliente_selezionato = self.controller.get_cliente_by_index(selected)
            self.vista_cliente = VistaCliente(cliente_selezionato)
            self.vista_cliente.show()

    def show_new_cliente(self):
        self.vista_inserisci_cliente = VistaInserisciCliente(self.controller, self.update_ui)
        self.vista_inserisci_cliente.show()

    def show_modifica_cliente(self):
        if len(self.list_view.selectedIndexes()) > 0:
            selected = self.list_view.selectedIndexes()[0].row()
            cliente_selezionato = self.controller.get_cliente_by_index(selected)
            self.vista_modifica_cliente = VistaModificaCliente(cliente_selezionato, self.update_ui)
            self.vista_modifica_cliente.show()

    def show_elimina_cliente(self):
        if len(self.list_view.selectedIndexes()) > 0:
            selected = self.list_view.selectedIndexes()[0].row()
            cliente_selezionato = self.controller.get_cliente_by_index(selected)
            self.controller.rimuovi_cliente_by_id(cliente_selezionato.get_id_cliente())
            self.update_ui()
            QMessageBox.critical(self, 'Eliminato', "Il cliente: {} {} e' stato eliminato".format(cliente_selezionato.nome,
                                                                                                    cliente_selezionato.cognome),
                                     QMessageBox.Ok,
                                     QMessageBox.Ok)

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for cliente in self.controller.get_lista_clienti():
            item = QStandardItem()
            item.setText(cliente.nome + " " + cliente.cognome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(12)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def closeEvent(self, event):
        self.controller.save_data()