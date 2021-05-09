class Oggetto:
    def __init__(self, id, nome, proprietario, prezzo, data_esposizione, descrizione, categoria):
        # da modificiare id
        self.id = id
        self.nome = nome
        self.proprietario = proprietario
        self.prezzo = prezzo
        self.data_esposizione = data_esposizione
        self.descrizione = descrizione
        self.categoria = categoria

    def set_proprietario(self, cliente):
        self.proprietario = cliente

    def set_prezzo(self, prezzo):
        self.prezzo = prezzo

    def set_data_esposizione(self, data_esposizione):
        self.data_esposizione = data_esposizione

    def set_descrizione(self, descrizione):
        self.descrizione = descrizione