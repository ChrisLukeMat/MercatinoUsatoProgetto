import os
import pickle


class Transazione:
    cnt = 0
    cod_transazione = 0
    def __init__(self, oggetto_venduto, acquirente, data_vendita):
        self.oggetto_venduto = oggetto_venduto
        self.acquirente = acquirente
        self.data_vendita = data_vendita
        if Transazione.cnt == 0:
            self.aggiorna_codice()
            Transazione.cnt += 1
        self.id_transazione = self.cod_transazione + 1
        self.id_transazione = str(self.id_transazione) + "t"
        Transazione.cod_dipendente += 1

    def aggiorna_saldo(self):
        saldo_parziale = self.oggetto_venduto.get_prezzo() / 2
        self.acquirente.set_saldo(self.acquirente.get_saldo() + saldo_parziale)

    def get_oggetto_venduto(self):
        return self.oggetto_venduto

    def get_acquirente(self):
        return self.acquirente

    def get_data_vendita(self):
        return self.data_vendita

    def get_id_transazione(self):
        return self.id_transazione

    def aggiorna_codice(self):
        if os.path.isfile('listatransazioni/data/lista_transazioni_salvata.pickle'):
            with open('listatransazioni/data/lista_transazioni_salvata.pickle', 'rb') as f:
                lista_transazioni = pickle.load(f)
                if len(lista_transazioni) != 0:
                    for transazione in lista_transazioni:
                        codice = transazione.get_id_transazione()
                    Transazione.cod_transazione = int(str(codice).split('t')[0])