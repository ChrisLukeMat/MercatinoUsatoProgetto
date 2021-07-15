import os
import pickle
from datetime import *

class Catalogo():
    def __init__(self):
        self.catalogo = []
        if os.path.isfile('catalogo/data/catalogo_salvato.pickle'):
            with open('catalogo/data/catalogo_salvato.pickle', 'rb') as f:
                catalogo_salvato = pickle.load(f)
            self.catalogo = catalogo_salvato
            for oggetto in self.catalogo:
                if not oggetto.sconto25:
                    if date.today() - oggetto.data_esposizione > timedelta(days = 30):
                        oggetto.sconto25 = True
                        oggetto.prezzo = oggetto.prezzo - (25/100 * oggetto.prezzo)

                if not oggetto.sconto50:
                    if date.today() - oggetto.data_esposizione > timedelta(days = 60):
                        oggetto.sconto50 = True
                        oggetto.prezzo = oggetto.prezzo * 100 / (100 - 25)
                        oggetto.prezzo = oggetto.prezzo - (50/100 * oggetto.prezzo)

                oggetto.prezzo = round(oggetto.prezzo, 2)

            self.save_data()

    def aggiungi_oggetto(self, oggetto):
        self.catalogo.append(oggetto)

    def rimuovi_oggetto_by_id(self, id):
        for oggetto in self.catalogo:
            if oggetto.id == id:
                self.catalogo.remove(oggetto)
                return True
        return False

    def get_oggetto_by_index(self, index):
        return self.catalogo[index]

    def get_catalogo(self):
        return self.catalogo

    def save_data(self):
        with open('catalogo/data/catalogo_salvato.pickle', 'wb') as handle:
            pickle.dump(self.catalogo, handle, pickle.HIGHEST_PROTOCOL)