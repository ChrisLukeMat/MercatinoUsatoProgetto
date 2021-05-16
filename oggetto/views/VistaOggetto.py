from PyQt5.QtGui import QTextFormat
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QFrame, QSpacerItem

from oggetto.controller.ControllerOggetto import ControllerOggetto


class VistaOggetto(QWidget):
    def __init__(self, oggetto, parent=None):
        super(VistaOggetto, self).__init__()
        self.controller = ControllerOggetto(oggetto)

        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()

        v_layout.addWidget(self.get_generic_label("Nome: "))
        v_layout.addWidget(self.get_generic_label("Prezzo: "))
        v_layout.addWidget(self.get_generic_label("Id: "))
        v_layout.addWidget(self.get_generic_label("Proprietario: "))
        v_layout.addWidget(self.get_generic_label("Data esposizione: "))
        v_layout.addWidget(self.get_generic_label("Descrizione: "))

        h_layout.addLayout(v_layout)

        v_layout2 = QVBoxLayout()

        v_layout2.addWidget(self.get_generic_label(str(self.controller.get_nome_oggetto())))
        v_layout2.addWidget(self.get_generic_label(str(self.controller.get_prezzo_oggetto()) + " €"))
        v_layout2.addWidget(self.get_generic_label(str(self.controller.get_id_oggetto())))

        nome_proprietario = self.controller.get_proprietario_oggetto().nome
        cognome_proprietario = self.controller.get_proprietario_oggetto().cognome
        v_layout2.addWidget(self.get_generic_label(nome_proprietario + " " + cognome_proprietario))

        v_layout2.addWidget(self.get_generic_label(str(self.controller.get_data_esposizione_oggetto())))

        label_descrizione = self.get_generic_label(self.controller.get_descrizione_oggetto())

        label_descrizione.setMaximumWidth(500)

        label_descrizione.setTextFormat(QTextFormat.FrameRightMargin)
        #label_descrizione.setMaximumWidth(200)
        #label_descrizione.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        #label_descrizione.setScaledContents(True)
        v_layout2.addWidget(label_descrizione)



        h_layout.addLayout(v_layout2)

       # buttons_layout = QVBoxLayout()
       # buttons_layout.addWidget(self.get_generic_button("Modifica", self.show_modifica_oggetto))
       # buttons_layout.addWidget(self.get_generic_button("Elimina", self.show_elimina_oggetto))
       # h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(400, 400)
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

    #def show_modifica_oggetto(self):
