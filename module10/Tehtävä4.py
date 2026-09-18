import random

class Auto:

    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka

    def kiihdytä(self, nopeuden_muutos):
        self.tämänhetkinen_nopeus += nopeuden_muutos
        if self.tämänhetkinen_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        if self.tämänhetkinen_nopeus < 0:
            self.tämänhetkinen_nopeus = 0

    def kulje(self, tuntimäärä):
        self.kuljettu_matka += self.tämänhetkinen_nopeus * tuntimäärä

class Kilpailu:
    def __init__(self, nimi, pituus, autot:list):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)
    def tulosta_tilanne(self):
        for auto in autot:
            print(f"Auto {auto.rekisteritunnus}, huippunopeus: {auto.huippunopeus}, nopeus: {auto.tämänhetkinen_nopeus}, matka: {auto.kuljettu_matka}")
        print("")
    def kilpailu_ohi(self):
        auto_on_edennyt_10000km = False
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                auto_on_edennyt_10000km = True
        return auto_on_edennyt_10000km


autot = []
for i in range(10):
        auto1 = Auto(f"ABC-{i+1}", random.randint(100, 200))
        autot.append(auto1)

kilpailu1 = Kilpailu("Suuri romuralli", 8000, autot)
kilpailu_ohi = False
tunnit = 0
while kilpailu_ohi == False:
    tunnit += 1
    kilpailu1.tunti_kuluu()
    kilpailu_ohi = kilpailu1.kilpailu_ohi()
    if tunnit % 10 == 0:
        print(f"Tunnit {tunnit}")
        kilpailu1.tulosta_tilanne()
else:
    print(f"Tunnit {tunnit}")
    kilpailu1.tulosta_tilanne()