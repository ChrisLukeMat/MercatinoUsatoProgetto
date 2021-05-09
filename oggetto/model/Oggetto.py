class Oggetto:
    cod_oggetto = 0
    def __init__(self, nome, proprietario, prezzo, data_esposizione, descrizione, categoria):
        self.id = self.cod_oggetto + 1
        str(self.id) + "o"
        self.cod_oggetto = self.cod_oggetto + 1

        self.nome = nome
        self.proprietario = proprietario
        self.prezzo = prezzo
        self.data_esposizione = data_esposizione
        self.descrizione = descrizione
        self.categoria = categoria

    def set_nome(self, nome):
        self.nome = nome

    def set_proprietario(self, cliente):
        self.proprietario = cliente

    def set_prezzo(self, prezzo):
        self.prezzo = prezzo

    def set_data_esposizione(self, data_esposizione):
        self.data_esposizione = data_esposizione

    def set_descrizione(self, descrizione):
        self.descrizione = descrizione