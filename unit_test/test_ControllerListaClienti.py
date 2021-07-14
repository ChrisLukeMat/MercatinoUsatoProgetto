from unittest import TestCase
from cliente.model.Cliente import Cliente
from listaclienti.controller.ControllerListaClienti import ControllerListaClienti

class TestControllerListaClienti(TestCase):

    cliente = Cliente("Luca", "Verdi", "provacf0123", "01/02/1992", "Milano", "3397843555", "Via Garibaldi 99")

    def test_aggiungi_cliente(self):
        controller = ControllerListaClienti()
        controller.aggiungi_cliente(self.cliente)
        self.assertIn(self.cliente, controller.get_lista_clienti())

    def test_rimuovi_cliente_by_id(self):
        controller = ControllerListaClienti()
        controller.aggiungi_cliente(self.cliente)
        id_cliente = self.cliente.get_id_cliente()
        controller.rimuovi_cliente_by_id(id_cliente)
        self.assertNotIn(self.cliente, controller.get_lista_clienti())

    def test_get_cliente_by_index(self):
        controller = ControllerListaClienti()
        controller.aggiungi_cliente(self.cliente)
        self.assertEquals(self.cliente, controller.get_cliente_by_index(len(controller.get_lista_clienti()) - 1))
