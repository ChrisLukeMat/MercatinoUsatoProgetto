import os
import pickle


class Catalogo():
    def __init__(self):
        self.catalogo = []

        if os.path.isfile('catalogo/data/catalogo_salvato.pickle'):
            print("esiste")
            with open('catalogo/data/catalogo_salvato.pickle', 'rb') as f:
                catalogo_salvato = pickle.load(f)
            self.model = catalogo_salvato

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
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)