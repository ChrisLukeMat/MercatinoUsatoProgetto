from listadipendenti.model.ListaDipendenti import ListaDipendenti

class ControllerListaDipendenti:
    def __init__(self):
        super(ControllerListaDipendenti, self).__init__()
        self.model = ListaDipendenti()

    def aggiungi_dipendente(self, dipendente):
        self.model.aggiungi_dipendente(dipendente)

    def rimuovi_dipendente_by_id(self, id):
        return self.model.rimuovi_dipendente_by_id(id)

    def get_dipendente_by_index(self, index):
        return self.model.get_dipendente_by_index(index)

    def get_lista_dipendenti(self):
        return self.model.get_lista_dipendenti()

    def save_data(self):
        self.model.save_data()