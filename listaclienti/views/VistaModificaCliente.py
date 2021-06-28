from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QSpacerItem, QPushButton, QSizePolicy, \
    QMessageBox
import datetime as dt

from cliente.controller.ControllerCliente import ControllerCliente


class VistaModificaCliente(QWidget):
    def __init__(self, cliente, callback, parent=None):
        super(VistaModificaCliente, self).__init__(parent)

        #self.cliente = cliente
        self.controller = ControllerCliente(cliente)
        self.callback = callback

        v_layout = QVBoxLayout()
        v_layout.addWidget(QLabel("Nome"))
        self.text_nome = QLineEdit(self)
        self.text_nome.setText(cliente.get_nome())
        v_layout.addWidget(self.text_nome)

        v_layout.addWidget(QLabel("Cognome"))
        self.text_cognome = QLineEdit(self)
        self.text_cognome.setText(cliente.get_cognome())
        v_layout.addWidget(self.text_cognome)

        v_layout.addWidget(QLabel("Codice fiscale"))
        self.text_cf = QLineEdit(self)
        self.text_cf.setText(cliente.get_cf())
        v_layout.addWidget(self.text_cf)

        v_layout.addWidget(QLabel("Indirizzo"))
        self.text_indirizzo = QLineEdit(self)
        self.text_indirizzo.setText(cliente.get_indirizzo())
        v_layout.addWidget(self.text_indirizzo)

        v_layout.addWidget(QLabel("Telefono"))
        self.text_telefono = QLineEdit(self)
        self.text_telefono.setText(cliente.get_telefono())
        v_layout.addWidget(self.text_telefono)

        v_layout.addWidget(QLabel("Luogo nascita"))
        self.text_luogo_nascita = QLineEdit(self)
        self.text_luogo_nascita.setText(cliente.get_luogo_nascita())
        v_layout.addWidget(self.text_luogo_nascita)

        v_layout.addWidget(QLabel("Data nascita"))

        v_layout_giorno = QVBoxLayout()
        v_layout_giorno.addWidget(QLabel("Giorno"))
        self.text_giorno_nascita = QLineEdit(self)
        self.text_giorno_nascita.setText(str(cliente.get_data_nascita().day))
        v_layout_giorno.addWidget(self.text_giorno_nascita)

        v_layout_mese = QVBoxLayout()
        v_layout_mese.addWidget(QLabel("Mese"))
        self.text_mese_nascita = QLineEdit(self)
        self.text_mese_nascita.setText(str(cliente.get_data_nascita().month))
        v_layout_mese.addWidget(self.text_mese_nascita)

        v_layout_anno = QVBoxLayout()
        v_layout_anno.addWidget(QLabel("Anno"))
        self.text_anno_nascita = QLineEdit(self)
        self.text_anno_nascita.setText(str(cliente.get_data_nascita().year))
        v_layout_anno.addWidget(self.text_anno_nascita)

        h_layout = QHBoxLayout()
        h_layout.addLayout(v_layout_giorno)
        h_layout.addLayout(v_layout_mese)
        h_layout.addLayout(v_layout_anno)

        v_layout.addLayout(h_layout)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.modifica_cliente)
        v_layout.addWidget(btn_ok)

        self.setLayout(v_layout)
        self.resize(300, 450)
        self.setWindowTitle('Modifica cliente')

    def modifica_cliente(self):
        nome = self.text_nome.text()
        cognome = self.text_cognome.text()
        cf = self.text_cf.text()
        giorno_nascita = self.text_giorno_nascita.text()
        mese_nascita = self.text_mese_nascita.text()
        anno_nascita = self.text_anno_nascita.text()
        luogo_nascita = self.text_luogo_nascita.text()
        telefono = self.text_telefono.text()
        indirizzo = self.text_indirizzo.text()

        if nome == "" or cognome == "" or cf == "" or giorno_nascita == "" or luogo_nascita == "" or telefono == "" \
                or indirizzo == "" or mese_nascita == "" or anno_nascita == "":
            QMessageBox.critical(self, 'Errore', "Per favore, inserisci tutte le informazioni richieste",
                                 QMessageBox.Ok, QMessageBox.Ok)
        else:
            try:
                data_nascita = dt.date(int(anno_nascita), int(mese_nascita), int(giorno_nascita))
                self.controller.set_nome(nome)
                self.controller.set_cognome(cognome)
                self.controller.set_cf(cf)
                self.controller.set_telefono(telefono)
                self.controller.set_indirizzo(indirizzo)
                self.controller.set_data_nascita(data_nascita)
                self.controller.set_luogo_nascita(luogo_nascita)
                '''self.cliente.set_nome(nome)
                self.cliente.set_cognome(cognome)
                self.cliente.set_cf(cf)
                self.cliente.set_telefono(telefono)
                self.cliente.set_indirizzo(indirizzo)
                self.cliente.set_data_nascita(data_nascita)
                self.cliente.set_luogo_nascita(luogo_nascita)'''
                self.callback()
                self.close()
            except ValueError:
                QMessageBox.critical(self, 'Errore', "Indicare valori corretti per la data!",
                                     QMessageBox.Ok, QMessageBox.Ok)
            except IndexError:
                QMessageBox.critical(self, 'Errore', "Indicare valori corretti per la data!",
                                     QMessageBox.Ok, QMessageBox.Ok)
            except AttributeError:
                QMessageBox.critical(self, 'Errore', "Indicare valori corretti per la data!",
                                     QMessageBox.Ok, QMessageBox.Ok)