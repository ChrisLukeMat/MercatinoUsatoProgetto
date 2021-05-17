class ControllerTransazione:
    def __init__(self, vendita):
        self.model = vendita

    def aggiorna_saldo(self):
        return self.model.aggiorna_saldo()

    def get_oggetto_venduto(self):
        return self.model.get_oggetto_venduto()

    def get_acquirente(self):
        return self.model.get_acquirente()

    def get_data_vendita(self):
        return self.model.get_data_vendita()

    def get_id_transazione(self):
        return self.model.get_id_transazione()