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

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti, tämänhetkinen_nopeus=0, kuljettu_matka=0):
        super().__init__(rekisteritunnus, huippunopeus, tämänhetkinen_nopeus, kuljettu_matka)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko, tämänhetkinen_nopeus=0, kuljettu_matka=0):
        super().__init__(rekisteritunnus, huippunopeus, tämänhetkinen_nopeus, kuljettu_matka)
        self.bensatankin_koko = bensatankin_koko

sähköauto = Sähköauto("ABC-15", 180, {52.5})
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, {32,3})

sähköauto.kiihdytä(100)
polttomoottoriauto.kiihdytä(100)

sähköauto.kulje(3)
polttomoottoriauto.kulje(3)

print(f"Säköauto: {sähköauto.kuljettu_matka}")
print(f"Polttomoottoriauto: {polttomoottoriauto.kuljettu_matka}")