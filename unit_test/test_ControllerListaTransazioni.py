from unittest import TestCase
from transazione.model.Transazione import Transazione
from cliente.model.Cliente import Cliente
from oggetto.model.Oggetto import Oggetto

class TestControllerListaTransazioni(TestCase):

    cliente1 = Cliente("Max", "Bonci", "provacf98765", "10/04/1999", "Palermo", "3357689777", "Via Ciao 20")
    cliente2 = Cliente("Marco", "Gialli", "codfiscale99999", "29/11/1997", "Venezia", "3337895488", "Via Prova 15")
    oggetto = Oggetto("Libro", cliente1, 4.99, "15/06/2021", "Il Visconte Dimezzato", "Lettura")
    transazione = Transazione(oggetto, cliente2, "21/06/2021")

    def test_aggiungi_transazione(self):
        self.lista_transazioni = []
        self.lista_transazioni.append(self.transazione)
        self.assertIn(self.transazione, self.lista_transazioni)

    def test_rimuovi_transazione_by_id(self):
        self.lista_transazioni = []
        self.lista_transazioni.append(self.transazione)
        self.id_transazione = '1t'
        for transazione in self.lista_transazioni:
            if transazione.get_id_transazione() == self.id_transazione:
                self.lista_transazioni.remove(transazione)
        self.assertNotIn(self.transazione, self.lista_transazioni)

    def test_get_transazione_by_index(self):
        self.lista_transazioni = []
        self.lista_transazioni.append(self.transazione)
        self.assertEquals(self.transazione, self.lista_transazioni[0])