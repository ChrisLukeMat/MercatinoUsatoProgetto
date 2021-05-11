from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy

from oggetto.controller.ControllerOggetto import ControllerOggetto


class VistaOggetto(QWidget):
    def __init__(self, oggetto, parent=None):
        super(VistaOggetto, self).__init__()
        self.controller = ControllerOggetto(oggetto)

        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()

        v_layout.addWidget(self.get_generic_label("Nome: " + self.controller.get_nome_oggetto()))
        v_layout.addWidget(self.get_generic_label("Prezzo: " + self.controller.get_prezzo_oggetto() + "€"))
        v_layout.addWidget(self.get_generic_label("Id: " + str(self.controller.get_id_oggetto())))
        v_layout.addWidget(self.get_generic_label("Proprietario: " + self.controller.get_proprietario_oggetto()))
        v_layout.addWidget(self.get_generic_label("Data esposizione: " + self.controller.get_data_esposizione_oggetto()))
        v_layout.addWidget(self.get_generic_label("Descrizione: " + self.controller.get_descrizione_oggetto()))

        h_layout.addLayout(v_layout)

        buttons_layout = QVBoxLayout()
       # buttons_layout.addWidget(self.get_generic_button("Modifica", self.show_modifica_oggetto))
       # buttons_layout.addWidget(self.get_generic_button("Elimina", self.show_elimina_oggetto))
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(500,400)
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
