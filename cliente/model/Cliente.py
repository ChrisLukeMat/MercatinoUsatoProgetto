class Cliente:
    cod_cliente = 0
    def __init__(self, nome, cognome, cf, data_nascita, luogo_nascita, telefono, indirizzo):
        self.nome = nome
        self.cognome = cognome
        self.cf = cf
        self.data_nascita = data_nascita
        self.luogo_nascita = luogo_nascita
        self.telefono = telefono
        self.indirizzo = indirizzo
        self.id_cliente = self.cod_cliente + 1
        self.id_cliente = str(self.id_cliente) + "c"
        self.cod_cliente += 1

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_cognome(self, cognome):
        self.cognome = cognome

    def get_cognome(self):
        return self.cognome

    def set_cf(self, cf):
        self.cf = cf

    def get_cf(self):
        return self.cf

    def set_data_nascita(self, data_nascita):
        self.data_nascita = data_nascita

    def get_data_nascita(self):
        return self.data_nascita

    def set_luogo_nascita(self, luogo_nascita):
        self.luogo_nascita = luogo_nascita

    def get_luogo_nascita(self):
        return self.luogo_nascita

    def set_telefono(self, telefono):
        self.telefono = telefono

    def get_telefono(self):
        return self.telefono

    def set_indirizzo(self, indirizzo):
        self.indirizzo = indirizzo

    def get_indirizzo(self):
        return self.indirizzo

    def get_id_cliente(self):
        return self.id_cliente


