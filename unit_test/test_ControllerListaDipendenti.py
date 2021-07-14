from unittest import TestCase
from dipendente.model.Dipendente import Dipendente
from listadipendenti.controller.ControllerListaDipendenti import ControllerListaDipendenti


class TestControllerListaDipendenti(TestCase):

    dipendente = Dipendente("Lorenzo", "Rossi", "abcdef12345", "12/12/2012", "Roma", "3325476889", "Via Milano 12", "pippo", "bomba8")

    def test_aggiungi_dipendente(self):
        controller = ControllerListaDipendenti()
        controller.aggiungi_dipendente(self.dipendente)
        self.assertIn(self.dipendente, controller.get_lista_dipendenti())

    def test_rimuovi_dipendente_by_id(self):
        controller = ControllerListaDipendenti()
        controller.aggiungi_dipendente(self.dipendente)
        id_dipendente = self.dipendente.get_id_dipendente()
        controller.rimuovi_dipendente_by_id(id_dipendente)
        self.assertNotIn(self.dipendente, controller.get_lista_dipendenti())


    def test_get_dipendente_by_index(self):
        controller = ControllerListaDipendenti()
        controller.aggiungi_dipendente(self.dipendente)
        self.assertEquals(self.dipendente,
                          controller.get_dipendente_by_index(len(controller.get_lista_dipendenti()) - 1))
