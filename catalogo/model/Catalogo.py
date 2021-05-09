class Catalogo():
    def __init__(self):
        self.catalogo = []

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