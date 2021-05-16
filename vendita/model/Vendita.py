class Vendita:
    def __init__(self, oggetto_venduto, acquirente, data_vendita):
        self.oggetto_venduto = oggetto_venduto
        self.acquirente = acquirente
        self.data_vendita = data_vendita

    def aggiorna_saldo(self):
        saldo_parziale = self.oggetto_venduto.get_prezzo() / 2
        self.acquirente.set_saldo(self.acquirente.get_saldo() + saldo_parziale)

    def get_oggetto_venduto(self):
        return self.oggetto_venduto

    def get_acquirente(self):
        return self.acquirente

    def get_data_vendita(self):
        return self.data_vendita