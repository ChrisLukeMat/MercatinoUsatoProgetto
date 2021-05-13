import os
import pickle

class ListaClienti:
    def __init__(self):
        self.lista_clienti = []
        if os.path.isfile('listaclienti/data/lista_clienti_salvata.pickle'):
            with open('listaclienti/data/lista_clienti_salvata.pickle', 'rb') as f:
                self.lista_clienti = pickle.load(f)

    def aggiungi_cliente(self, cliente):
        self.lista_clienti.append(cliente)

    def rimuovi_cliente_by_id(self, id_cliente):
        for cliente in self.lista_clienti:
            if cliente.get_id_cliente() == id_cliente:
                self.lista_clienti.remove(cliente)
                return True
        return False

    def get_cliente_by_index(self, index):
        return self.lista_clienti[index]

    def get_lista_clienti(self):
        return self.lista_clienti

    def save_data(self):
        with open('listaclienti/data/lista_clienti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_clienti, handle, pickle.HIGHEST_PROTOCOL)