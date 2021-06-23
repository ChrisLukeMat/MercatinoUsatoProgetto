from PyQt5.QtGui import QTextFormat, QPalette
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from oggetto.controller.ControllerOggetto import ControllerOggetto


class VistaOggetto(QWidget):
    def __init__(self, oggetto, parent=None):
        super(VistaOggetto, self).__init__()
        self.controller = ControllerOggetto(oggetto)

        v_layout_finale = QVBoxLayout()
        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()
        h_layout_desc = QHBoxLayout()

        v_layout.addWidget(self.get_generic_label("Nome: "))
        v_layout.addWidget(self.get_generic_label("Prezzo: "))
        v_layout.addWidget(self.get_generic_label("Id: "))
        v_layout.addWidget(self.get_generic_label("Proprietario: "))
        v_layout.addWidget(self.get_generic_label("Data esposizione: "))

        h_layout.addLayout(v_layout)

        v_layout2 = QVBoxLayout()
        v_layout2.addWidget(self.get_generic_label(str(self.controller.get_nome_oggetto())))
        v_layout2.addWidget(self.get_generic_label(str(self.controller.get_prezzo_oggetto()) + " €"))
        v_layout2.addWidget(self.get_generic_label(str(self.controller.get_id_oggetto())))

        nome_proprietario = self.controller.get_proprietario_oggetto().nome
        cognome_proprietario = self.controller.get_proprietario_oggetto().cognome
        id_proprietario = self.controller.get_proprietario_oggetto().get_id_cliente()
        v_layout2.addWidget(self.get_generic_label(nome_proprietario + " " + cognome_proprietario + " " + id_proprietario))

        v_layout2.addWidget(self.get_generic_label(self.controller.get_data_esposizione_oggetto().strftime("%d-%m-%Y")))

        h_layout.addLayout(v_layout2)

        label_nome_descrizione = self.get_generic_label("Descrizione: ")
        label_nome_descrizione.setAlignment(Qt.AlignTop)
        h_layout_desc.addWidget(label_nome_descrizione)

        descrizione_ogg = self.controller.get_descrizione_oggetto()

        for i in range(1, len(descrizione_ogg)):
            if i % 30 == 0:
                descrizione_ogg = descrizione_ogg[:i] + "\n" + descrizione_ogg[i:]

        label_descrizione = self.get_generic_label(descrizione_ogg)
        label_descrizione.setAlignment(Qt.AlignTop)
        h_layout_desc.addWidget(label_descrizione)

        v_layout_finale.addLayout(h_layout)
        v_layout_finale.addLayout(h_layout_desc)
        self.setLayout(v_layout_finale)
        self.resize(600, 300)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setWindowTitle("{}".format(oggetto.nome))

    def get_generic_label(self, text):
        label = QLabel(str(text))
        label.setStyleSheet("background-color: rgba(52,52,52,50%); border-radius: 7px; border: 1px solid black;")
        return label

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button