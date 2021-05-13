from cliente.model.Cliente import Cliente

class ControllerCliente:
    def __init__(self, cliente):
        self.model = cliente

    def set_nome(self, nome):
        self.model.set_nome(nome)

    def get_nome(self):
        return self.model.get_nome()

    def set_cognome(self, cognome):
        self.model.set_cognome(cognome)

    def get_cognome(self):
        return self.model.get_cognome()

    def set_cf(self, cf):
        self.model.set_cf(cf)

    def get_cf(self):
        return self.model.get_cf()

    def set_data_nascita(self, data_nascita):
        self.model.set_data_nascita(data_nascita)

    def get_data_nascita(self):
        return self.model.get_data_nascita()

    def set_luogo_nascita(self, luogo_nascita):
        self.model.set_luogo_nascita(luogo_nascita)

    def get_luogo_nascita(self):
        return self.model.get_luogo_nascita()

    def set_indirizzo(self, indirizzo):
        self.model.set_indirizzo(indirizzo)

    def get_indirizzo(self):
        return self.model.get_indirizzo()

    def set_telefono(self, telefono):
        self.model.set_telefono(telefono)

    def get_telefono(self):
        return self.model.get_telefono()

    def get_id_cliente(self):
        return self.model.get_id_cliente()