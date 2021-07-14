from unittest import TestCase

from catalogo.controller.ControllerCatalogo import ControllerCatalogo
from oggetto.model.Oggetto import Oggetto
from cliente.model.Cliente import Cliente

class TestControllerCatalogo(TestCase):

    cliente = Cliente("Luca", "Verdi", "provacf0123", "01/02/1992", "Milano", "3397843555", "Via Garibaldi 99")
    oggetto = Oggetto("Armadio", cliente, 14.99, "21/06/2021", "Condizioni ottime", "Arredamento")

    def test_aggiungi_oggetto(self):
        controller = ControllerCatalogo()
        controller.aggiungi_oggetto(self.oggetto)
        self.assertIn(self.oggetto, controller.get_catalogo())

    '''def test_rimuovi_oggetto_by_id(self):
        self.catalogo = []
        self.catalogo.append(self.oggetto)
        self.id_ogg = '1o'
        for oggetto in self.catalogo:
            if oggetto.id == self.id_ogg:
                self.catalogo.remove(oggetto)
        self.assertNotIn(self.oggetto, self.catalogo)'''

    def test_rimuovi_oggetto_by_id(self):
        controller = ControllerCatalogo()
        controller.aggiungi_oggetto(self.oggetto)
        id_oggetto = self.oggetto.id
        controller.rimuovi_oggetto_by_id(id_oggetto)
        self.assertNotIn(self.oggetto, controller.get_catalogo())

    def test_get_oggetto_by_index(self):
        controller = ControllerCatalogo()
        controller.aggiungi_oggetto(self.oggetto)
        self.assertEquals(self.oggetto, controller.get_oggetto_by_index(len(controller.get_catalogo()) - 1))