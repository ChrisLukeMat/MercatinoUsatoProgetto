from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSizePolicy, QSpacerItem, QPushButton, QTextEdit


class VistaModificaOggetto(QWidget):
    def __init__(self, oggetto, callback, parent=None):
        super(VistaModificaOggetto, self).__init__()
        self.oggetto = oggetto
        self.callback = callback

        v_layout = QVBoxLayout()
        v_layout.addWidget(QLabel("Nome"))
        self.text_nome = QLineEdit(self)
        self.text_nome.setText(self.oggetto.nome)
        v_layout.addWidget(self.text_nome)

        v_layout.addWidget(QLabel("Prezzo"))
        self.text_prezzo = QLineEdit(self)
        v_layout.addWidget(self.text_prezzo)

        v_layout.addWidget(QLabel("Proprietario"))
        self.text_proprietario = QLineEdit(self)
        v_layout.addWidget(self.text_proprietario)

        v_layout.addWidget(QLabel("Descrizione"))
        self.text_descrizione = QTextEdit(self)
        self.text_descrizione.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.text_descrizione.setAlignment(Qt.AlignTop)
        self.text_descrizione.setText(self.oggetto.descrizione)
        v_layout.addWidget(self.text_descrizione)

        v_layout.addWidget(QLabel("Categoria"))
        self.text_categoria = QLineEdit(self)
        v_layout.addWidget(self.text_categoria)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.modifica_oggetto)
        v_layout.addWidget(btn_ok)

        self.setLayout(v_layout)
        self.resize(300, 450)
        self.setWindowTitle('Nuovo Oggetto')

    def modifica_oggetto(self):
        pass