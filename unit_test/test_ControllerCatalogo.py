from unittest import TestCase
from oggetto.model.Oggetto import Oggetto
from cliente.model.Cliente import Cliente

class TestControllerCatalogo(TestCase):

    cliente = Cliente("Luca", "Verdi", "provacf0123", "01/02/1992", "Milano", "3397843555", "Via Garibaldi 99")
    oggetto = Oggetto("Armadio", cliente, 14.99, "21/06/2021", "Condizioni ottime", "Arredamento")

    def test_aggiungi_oggetto(self):
        self.catalogo = []
        self.catalogo.append(self.oggetto)
        self.assertIn(self.oggetto, self.catalogo)

    def test_rimuovi_oggetto_by_id(self):
        self.catalogo = []
        self.catalogo.append(self.oggetto)
        self.id_ogg = '1o'
        for oggetto in self.catalogo:
            if oggetto.id == self.id_ogg:
                self.catalogo.remove(oggetto)
        self.assertNotIn(self.oggetto, self.catalogo)

    def test_get_oggetto_by_index(self):
        self.catalogo = []
        self.catalogo.append(self.oggetto)
        self.assertEquals(self.oggetto, self.catalogo[0])