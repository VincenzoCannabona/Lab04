class Cabina:
    def __init__(self, codice, letti, ponte, prezzo):
        self.codice = codice
        self.letti = letti
        self.ponte = ponte
        self.prezzo = int(prezzo)

    def prezzo_totale(self):
        return self.prezzo

    def __lt__(self, other):
        # confronto tra cabine in base al prezzo
        return self.prezzo_totale() < other.prezzo_totale()

    def __str__(self):
        return f'cabina {self.codice}, {self.letti} letti, ponte {self.ponte},prezzo {self.prezzo_totale()}'

class Cabina_animali(Cabina):
    def __init__(self, codice,letti, ponte, prezzo, num_animali):
        super().__init__(codice, letti, ponte, prezzo)
        self.num_animali = int(num_animali)
        self.sovrapprezzo = float(prezzo) * (1 + 0.10 * int(num_animali))

    def prezzo_totale(self):
        return int(self.prezzo)+int(self.sovrapprezzo)

    def __str__(self):
        return f"Cabina {self.codice}, {self.letti} letti, ponte {self.ponte},prezzo {self.prezzo_totale()}, numero animali permessi {self.num_animali}"

class Cabina_deluxe(Cabina):
    def __init__(self, codice, letti, ponte, prezzo, stile):
        super().__init__(codice, letti, ponte, prezzo)
        self.sovrapprezzo = float(prezzo) * 1.20
        self.stile = stile

    def prezzo_totale(self):
        return int(self.prezzo)+int(self.sovrapprezzo)

    def __str__(self):
        return f"Cabina {self.codice}, {self.letti} letti, ponte {self.ponte},prezzo {self.prezzo_totale()}, stile {self.stile}"
