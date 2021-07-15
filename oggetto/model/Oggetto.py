import os
import pickle

class Oggetto:
    cnt = 0
    cod_oggetto = 0
    def __init__(self, nome, proprietario, prezzo, data_esposizione, descrizione, categoria):
        self.sconto25 = False
        self.sconto50 = False
        self.nome = nome
        self.proprietario = proprietario
        self.prezzo = prezzo
        self.data_esposizione = data_esposizione
        self.descrizione = descrizione
        self.categoria = categoria
        if Oggetto.cnt == 0:
            self.aggiorna_codice()
            Oggetto.cnt += 1
        self.id = self.cod_oggetto + 1
        self.id = str(self.id) + "o"
        Oggetto.cod_oggetto += 1

    def set_nome(self, nome):
        self.nome = nome

    def set_proprietario(self, cliente):
        self.proprietario = cliente

    def set_prezzo(self, prezzo):
        self.prezzo = prezzo

    def set_data_esposizione(self, data_esposizione):
        self.data_esposizione = data_esposizione

    def set_descrizione(self, descrizione):
        self.descrizione = descrizione

    def set_categoria(self, categoria):
        self.categoria = categoria

    def aggiorna_codice(self):
        if os.path.isfile('catalogo/data/catalogo_salvato.pickle'):
            with open('catalogo/data/catalogo_salvato.pickle', 'rb') as f:
                catalogo = pickle.load(f)
                if len(catalogo) != 0:
                    for oggetto in catalogo:
                        codice = oggetto.id
                    Oggetto.cod_oggetto= int(str(codice).split('o')[0])