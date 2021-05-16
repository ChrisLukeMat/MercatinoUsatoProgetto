from PyQt5.QtGui import QTextFormat
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QFrame, QSpacerItem

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
        v_layout2.addWidget(self.get_generic_label(nome_proprietario + " " + cognome_proprietario))

        v_layout2.addWidget(self.get_generic_label(self.controller.get_data_esposizione_oggetto().strftime("%d-%m-%Y")))

        h_layout.addLayout(v_layout2)

        h_layout_desc.addWidget(self.get_generic_label("Descrizione: "))
        descrizione_ogg = self.controller.get_descrizione_oggetto()

        for i in range(0, len(descrizione_ogg)):
            if i % 25 == 0:
                descrizione_ogg = descrizione_ogg[:i] + "\n" + descrizione_ogg[i:]

        label_descrizione = self.get_generic_label(descrizione_ogg)
        h_layout_desc.addWidget(label_descrizione)

        v_layout_finale.addLayout(h_layout)
        v_layout_finale.addLayout(h_layout_desc)
        v_layout_finale.addStretch()

        self.setLayout(v_layout_finale)
        self.resize(700, 300)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setWindowTitle("{}".format(oggetto.nome))#provare senza format

    def get_generic_label(self, text):
        label = QLabel(str(text))
        font = label.font()
        font.setPointSize(20)
        label.setFont(font)
        return label

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button