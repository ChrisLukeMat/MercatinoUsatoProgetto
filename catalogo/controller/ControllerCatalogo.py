from catalogo.model.Catalogo import Catalogo

class ControllerCatalogo():
    def __init__(self):
        super(ControllerCatalogo, self).__init__()
        self.model = Catalogo

    def aggiungi_oggetto(self, oggetto):
        self.model.aggiungi_oggetto(oggetto)

    def rimuovi_oggetto_by_id(self, id):
        return self.model.rimuovi_oggetto_by_id(id)

    def get_oggetto_by_index(self, index):
        return self.model.get_oggetto_by_index(index)

    def get_catalogo(self):
        return self.model.get_catalogo()

