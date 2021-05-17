from listatransazioni.model.ListaTransazioni import ListaTransazioni


class ControllerListaTransazioni:
    def __init__(self):
        super(ControllerListaTransazioni, self).__init__()
        self.model = ListaTransazioni()

    def aggiungi_transazione(self, transazione):
        self.model.aggiungi_transazione(transazione)

    def rimuovi_transazione_by_id(self, id):
        return self.model.rimuovi_transazione_by_id(id)

    def get_transazione_by_index(self, index):
        return self.model.get_transazione_by_index(index)

    def get_lista_transazioni(self):
        return self.model.get_lista_transazioni()

    def save_data(self):
        self.model.save_data()