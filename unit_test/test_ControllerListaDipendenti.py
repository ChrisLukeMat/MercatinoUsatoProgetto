from unittest import TestCase
from dipendente.model.Dipendente import Dipendente


class TestControllerListaDipendenti(TestCase):

    dipendente = Dipendente("Lorenzo", "Rossi", "abcdef12345", "12/12/2012", "Roma", "3325476889", "Via Milano 12")

    def test_aggiungi_dipendente(self):
        self.lista_dipendenti = []
        self.lista_dipendenti.append(self.dipendente)
        self.assertIn(self.dipendente, self.lista_dipendenti)

    def test_rimuovi_dipendente_by_id(self):
        self.lista_dipendenti = []
        self.lista_dipendenti.append(self.dipendente)
        self.id_dip = '1d'
        for dipendente in self.lista_dipendenti:
            if dipendente.get_id_dipendente() == self.id_dip:
                self.lista_dipendenti.remove(dipendente)
        self.assertNotIn(self.dipendente, self.lista_dipendenti)

    def test_get_dipendente_by_index(self):
        self.lista_dipendenti = []
        self.lista_dipendenti.append(self.dipendente)
        self.assertEquals(self.dipendente, self.lista_dipendenti[0])