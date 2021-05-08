class ControllerOggetto():
    def __init__(self, oggetto):
        self.model = oggetto

    def get_id_oggetto(self):
        return self.model.id
        
    def get_proprietario_oggetto(self):
        return self.model.proprietario

    def get_prezzo_oggetto(self):
        return self.model.prezzo

    def get_data_esposizione_oggetto(self):
        return self.model.data_esposizione

    def get_descrizione_oggetto(self):
        return self.model.descrizione