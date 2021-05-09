import json
import os
import pickle

from catalogo.model.Catalogo import Catalogo

class ControllerCatalogo():
    def __init__(self):
        super(ControllerCatalogo, self).__init__()
        self.model = Catalogo()

        if os.path.isfile('catalogo/data/catalogo_salvato.pickle'):
            print("esiste")
            with open('catalogo/data/catalogo_salvato.pickle', 'rb') as f:
                catalogo_salvato = pickle.load(f)
            self.model = catalogo_salvato
        else:
            print("non esiste")
            with open('listaservizi/data/lista_servizi_iniziali.json') as f:
                lista_servizi_iniziale = json.load(f)
            for servizio in lista_servizi_iniziale:
                self.model.aggiungi_servizio(
                    Servizio(servizio["id"], servizio["nome"], servizio["tipo"], servizio["posizione"],
                             servizio["prezzo"]))
            with open('listaservizi/data/lista_servizi_salvata.pickle', 'wb') as handle:
                pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)


    def aggiungi_oggetto(self, oggetto):
        self.model.aggiungi_oggetto(oggetto)

    def rimuovi_oggetto_by_id(self, id):
        return self.model.rimuovi_oggetto_by_id(id)

    def get_oggetto_by_index(self, index):
        return self.model.get_oggetto_by_index(index)

    def get_catalogo(self):
        return self.model.get_catalogo()

