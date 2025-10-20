import csv
from cabine import Cabina, Cabina_deluxe, Cabina_animali
from passeggeri import Passeggero

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.nome=nome
        self.cabine=[]
        self.passeggeri=[]
        self.cabinaD=[]
        self.passeggeroD=[]
        self.assegnazioni={}

    """Aggiungere setter e getter se necessari"""
    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for riga in reader:
                    if len(riga)==3:
                        codice, nome, cognome = riga
                        passeggero= Passeggero(codice, nome, cognome)
                        self.passeggeri.append(passeggero)

                    elif len(riga)==4:
                        codice, letti, ponte, prezzo = riga
                        cabina= Cabina(codice, letti, ponte, prezzo)
                        self.cabine.append(cabina)

                    elif len(riga)==5:
                        if riga[4].isalpha():
                            codice, letti, ponte, prezzo, stile= riga
                            cabinaDeluxe= Cabina_deluxe(codice, letti, ponte, prezzo, stile)
                            self.cabine.append(cabinaDeluxe)
                        else:
                            codice, letti, ponte, prezzo, num_animali = riga
                            cabinaAnimali= Cabina_animali(codice, letti, ponte, prezzo, num_animali)
                            self.cabine.append(cabinaAnimali)


        except FileNotFoundError:
            raise Exception()


    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        trovata1=False
        for c in self.cabine:
            if codice_cabina==c.codice:
                trovata1 = True
                break
        if not trovata1:
            raise Exception("la cabina non esiste")

        trovata2 = False
        for p in self.passeggeri:
            if codice_passeggero == p.codice:
                trovata2 = True
                break
        if not trovata2:
            raise Exception("il passeggero non esiste")

        if codice_cabina not in self.cabinaD:       #posso usare not in in questo caso perche self.cabinaD ha solo i codici delle cabine
            self.cabinaD.append(codice_cabina)
        else:
            raise Exception("la cabina è già stata prenotata")

        if codice_passeggero not in self.passeggeroD:
            self.passeggeroD.append(codice_passeggero)
        else:
            raise Exception("il passeggero ha già una cabina assegnata")

        print (f"il passeggero {codice_passeggero} ha prenotato la cabina {codice_cabina}")
        tupla=(codice_passeggero,codice_cabina)
        self.assegnazioni[codice_passeggero] = codice_cabina


    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        return sorted(self.cabine)


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        for p in self.passeggeri:
            codice_p = p.codice
            if codice_p in self.assegnazioni:
                cabina = self.assegnazioni[codice_p]
                print(f"- {p.nome} (codice: {p.codice}) → cabina {cabina}")
            else:
                print(f"- {p.nome} (codice: {p.codice}) → nessuna cabina assegnata")

