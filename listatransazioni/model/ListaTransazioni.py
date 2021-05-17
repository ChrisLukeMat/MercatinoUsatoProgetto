import os
import pickle


class ListaTransazioni():
    def __init__(self):
        self.lista_transazioni = []
        if os.path.isfile('listatransazioni/data/lista_transazioni_salvata.pickle'):
            with open('listatransazioni/data/lista_transazioni_salvata.pickle', 'rb') as f:
                self.lista_transazioni = pickle.load(f)

    def aggiungi_transazione(self, transazione):
        self.lista_transazioni.append(transazione)

    def rimuovi_transazione_by_id(self, id_transazione):
        for transazione in self.lista_transazioni:
            if transazione.get_id_transazione() == id_transazione:
                self.lista_transazioni.remove(transazione)
                return True
        return False

    def get_transazione_by_index(self, index):
        return self.lista_transazioni[index]

    def get_lista_transazioni(self):
        return self.lista_transazioni

    def save_data(self):
        with open('listatransazioni/data/lista_transazioni_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_transazioni, handle, pickle.HIGHEST_PROTOCOL)