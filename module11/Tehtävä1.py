class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        print(f"{self.nimi} {self.kirjoittaja} {self.sivumäärä}")

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        print(f"{self.nimi} {self.päätoimittaja}")

julkaisu1 = Lehti("Aku Ankka,", "Aki Hyyppä")
julkaisu2 = Kirja("Hytti n:o 6,", "Rosa Liksom,", f"{200} sivua")

julkaisu1.tulosta_tiedot()
julkaisu2.tulosta_tiedot()