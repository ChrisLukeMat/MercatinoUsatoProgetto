import os
import pickle


class Dipendente:
    cnt = 0
    cod_dipendente = 0
    def __init__(self, nome, cognome, cf, data_nascita, luogo_nascita, telefono, indirizzo):
        self.nome = nome
        self.cognome = cognome
        self.cf = cf
        self.data_nascita = data_nascita
        self.luogo_nascita = luogo_nascita
        self.telefono = telefono
        self.indirizzo = indirizzo
        if Dipendente.cnt == 0:
            self.aggiorna_codice()
            Dipendente.cnt += 1
        self.id_dipendente = self.cod_dipendente + 1
        self.id_dipendente = str(self.id_dipendente) + "d"
        Dipendente.cod_dipendente += 1

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_cognome(self, cognome):
        self.cognome = cognome

    def get_cognome(self):
        return self.cognome

    def set_cf(self, cf):
        self.cf = cf

    def get_cf(self):
        return self.cf

    def set_data_nascita(self, data_nascita):
        self.data_nascita = data_nascita

    def get_data_nascita(self):
        return self.data_nascita

    def set_luogo_nascita(self, luogo_nascita):
        self.luogo_nascita = luogo_nascita

    def get_luogo_nascita(self):
        return self.luogo_nascita

    def set_telefono(self, telefono):
        self.telefono = telefono

    def get_telefono(self):
        return self.telefono

    def set_indirizzo(self, indirizzo):
        self.indirizzo = indirizzo

    def get_indirizzo(self):
        return self.indirizzo

    def get_id_dipendente(self):
        return self.id_dipendente

    def aggiorna_codice(self):
        if os.path.isfile('listadipendenti/data/lista_dipendenti_salvata.pickle'):
            with open('listadipendenti/data/lista_dipendenti_salvata.pickle', 'rb') as f:
                lista_dipendenti = pickle.load(f)
                if len(lista_dipendenti) != 0:
                    for dipendente in lista_dipendenti:
                        codice = dipendente.get_id_dipendente()
                    Dipendente.cod_dipendente = int(str(codice).split('d')[0])