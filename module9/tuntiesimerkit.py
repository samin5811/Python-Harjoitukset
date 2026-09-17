# class Auto:
#     pass
# class Opiskelija:
#     pass

# opiskelija1 = Opiskelija()

# opiskelija1.nimi = "Jaakko"
# opiskelija1.syntymävuosi = "2006"
# opiskelija1.keksiarvo = 1

# print(f"{opiskelija1.nimi} syntyi vuonna  {opiskelija1.syntymävuosi}")

# def laske_kahden_luvun_summa(luku1, luku2):
#     summa = luku1 + luku2
#     return summa

# yhteenlaskettu_summa = laske_kahden_luvun_summa(5, 10)

# print(f"Summa: {yhteenlaskettu_summa}")

class Hero:
    sankarien_määrä = 0

    def __init__(self, nimi, tyyppi, voima, aseääni, huudahdus="Hei!"):
        self.nimi = nimi
        self.tyyppi = tyyppi
        self.voima = voima
        self.huudahdus = huudahdus
        self.aseääni = aseääni
        Hero.sankarien_määrä += 1

    def huuda(self, kerrat=1):
        for i in range(kerrat):
            print(f"{self.huudahdus}")

    def ase(self):
        print(self.aseääni)

hero1 = Hero("Reinhardt", "Tankki", "Voimakas", "BONK", "AAAAARRGHHH")
hero2 = Hero("Tracer", "Vahingontekijä", "Nopea", "Bäng")

print(f"{hero1.nimi} on {hero1.tyyppi} ja hän on {hero1.voima}, hän sanoo {hero1.huudahdus}")
print(f"{hero2.nimi} on {hero2.tyyppi} ja hän on {hero2.voima}, hän sanoo {hero2.huudahdus}")

hero1.huuda()
hero2.huuda()

hero1.ase()
hero2.ase()

print(f"Sankarien määrä: {Hero.sankarien_määrä}")

class Pelaaja:
    def __init__(self, nimi, elämät=3, kolikot=0, pisteet=0):
        self.nimi = nimi
        self.elämät = elämät
        self.kolikot = kolikot
        self.pisteet = pisteet

pelaaja1 = Pelaaja("Mario")
print("")
print(pelaaja1.nimi)
print(pelaaja1.elämät)
print(pelaaja1.kolikot)
print(pelaaja1.pisteet)

class Merirosvolaiva:
    def __init__(self, nimi, tykkien_määrä, miehistön_määrä, kulta=0):
        self.nimi = nimi
        self.tykkien_määrä = tykkien_määrä
        self.miehistön_määrä = miehistön_määrä
        self.kulta = kulta
    def löydä_aarre(self, määrä):
        self.kulta += määrä
    def menetä_kultaa(self, määrä):
        self.kulta -= määrä
        if self.kulta < 0:
            self.kulta = 0
    def palkkaa_miehistöä(self, määrä):
        self.miehistön_määrä += määrä

laiva1 = Merirosvolaiva("Black Pearl", 12, 40)

laiva1.löydä_aarre(200)
laiva1.löydä_aarre(75)
laiva1.menetä_kultaa(100)
print("")
print(laiva1.nimi)
print(laiva1.tykkien_määrä)
print(laiva1.miehistön_määrä)
print(laiva1.kulta)