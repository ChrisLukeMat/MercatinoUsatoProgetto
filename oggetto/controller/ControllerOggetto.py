class ControllerOggetto():
    def __init__(self, oggetto):
        self.model = oggetto

    def get_nome_oggetto(self):
        return self.model.nome

    def set_nome_oggetto(self,nome):
        self.model.set_nome(nome)

    def get_id_oggetto(self):
        return self.model.id
        
    def get_proprietario_oggetto(self):
        return self.model.proprietario

    def set_proprietario_oggetto(self, oggetto):
        self.model.set_proprietario(oggetto)

    def get_prezzo_oggetto(self):
        return self.model.prezzo

    def set_prezzo_oggetto(self, prezzo):
        self.model.set_prezzo(prezzo)

    def get_data_esposizione_oggetto(self):
        return self.model.data_esposizione

    def set_data_esposizione_oggetto(self, data_esposizione):
        self.model.set_data_esposizione(data_esposizione)

    def get_descrizione_oggetto(self):
        return self.model.descrizione

    def set_descrizione_oggetto(self, descrizione):
        self.model.set_descrizione(descrizione)

    def get_categoria_oggetto(self):
        return self.model.categoria

    def set_categoria_oggetto(self,categoria):
        self.model.set_categoria(categoria)