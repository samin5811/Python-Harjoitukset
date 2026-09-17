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
auto = Auto(rekisteritunnus = "ABC-123", huippunopeus = 142)

# print(f"Rekisteritunnus: {auto.rekisteritunnus}")
# print(f"Huippunopeus: {auto.huippunopeus} km/h")
# print(f"Tämänhetkinen_nopeus: {auto.tämänhetkinen_nopeus} km/h")
# print(f"Kuljettu_matka {auto.kuljettu_matka} km")

# auto.kiihdytä(30)
# print(f"Tämänhetkinen_nopeus: {auto.tämänhetkinen_nopeus} km/h")
# auto.kiihdytä(70)
# print(f"Tämänhetkinen_nopeus: {auto.tämänhetkinen_nopeus} km/h")
# auto.kiihdytä(50)
# print(f"Tämänhetkinen_nopeus: {auto.tämänhetkinen_nopeus} km/h")
# auto.kiihdytä(-200)
# print(f"Tämänhetkinen_nopeus: {auto.tämänhetkinen_nopeus} km/h")