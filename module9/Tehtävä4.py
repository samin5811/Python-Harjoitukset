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

autot = []
for i in range(10):
        auto1 = Auto(f"ABC-{i+1}", random.randint(100, 200))
        autot.append(auto1)

def autot_tunnin_välein():
     for auto in autot:
          auto.kiihdytä(random.randint(-10, 15))
          auto.kulje(1)

auto_on_edennyt_10000km = True

while auto_on_edennyt_10000km:
     autot_tunnin_välein()
     for auto in autot:
          if auto.kuljettu_matka >= 10000:
               auto_on_edennyt_10000km = False
else:
    for auto in autot:
        print(f"Auto {auto.rekisteritunnus}, huippunopeus: {auto.huippunopeus}, nopeus: {auto.tämänhetkinen_nopeus}, matka: {auto.kuljettu_matka}")