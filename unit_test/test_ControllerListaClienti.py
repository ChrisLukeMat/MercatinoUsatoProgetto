from unittest import TestCase
from cliente.model.Cliente import Cliente

class TestControllerListaClienti(TestCase):

    cliente = Cliente("Luca", "Verdi", "provacf0123", "01/02/1992", "Milano", "3397843555", "Via Garibaldi 99")

    def test_aggiungi_cliente(self):
        self.lista_clienti = []
        self.lista_clienti.append(self.cliente)
        self.assertIn(self.cliente, self.lista_clienti)

    def test_rimuovi_cliente_by_id(self):
        self.lista_clienti = []
        self.lista_clienti.append(self.cliente)
        self.id_cliente = '1c'
        for cliente in self.lista_clienti:
            if cliente.get_id_cliente() == self.id_cliente:
                self.lista_clienti.remove(cliente)
        self.assertNotIn(self.cliente, self.lista_clienti)

    def test_get_cliente_by_index(self):
        self.lista_clienti = []
        self.lista_clienti.append(self.cliente)
        self.assertEquals(self.cliente, self.lista_clienti[0])