from unittest import TestCase

from listatransazioni.controller.ControllerListaTransazioni import ControllerListaTransazioni
from transazione.model.Transazione import Transazione
from cliente.model.Cliente import Cliente
from oggetto.model.Oggetto import Oggetto

class TestControllerListaTransazioni(TestCase):

    cliente1 = Cliente("Max", "Bonci", "provacf98765", "10/04/1999", "Palermo", "3357689777", "Via Ciao 20")
    cliente2 = Cliente("Marco", "Gialli", "codfiscale99999", "29/11/1997", "Venezia", "3337895488", "Via Prova 15")
    oggetto = Oggetto("Libro", cliente1, 4.99, "15/06/2021", "Il Visconte Dimezzato", "Lettura")
    transazione = Transazione(oggetto, cliente2, "21/06/2021")

    def test_aggiungi_transazione(self):
        controller = ControllerListaTransazioni()
        controller.aggiungi_transazione(self.transazione)
        self.assertIn(self.transazione, controller.get_lista_transazioni())

    def test_rimuovi_transazione_by_id(self):
        controller = ControllerListaTransazioni()
        controller.aggiungi_transazione(self.transazione)
        id_transazione = self.transazione.get_id_transazione()
        controller.rimuovi_transazione_by_id(id_transazione)
        self.assertNotIn(self.transazione, controller.get_lista_transazioni())


    def test_get_transazione_by_index(self):
        controller = ControllerListaTransazioni()
        controller.aggiungi_transazione(self.transazione)
        self.assertEquals(self.transazione, controller.get_transazione_by_index(len(controller.get_lista_transazioni()) - 1))