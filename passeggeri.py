class Passeggero:
    def __init__(self, codice, nome, cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome

    def __str__(self):
        return f"passeggero {self.codice}, nome {self.nome}, cognome {self.cognome}"