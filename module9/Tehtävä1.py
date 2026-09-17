class Auto:

    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka

auto = Auto(rekisteritunnus = "ABC-123", huippunopeus = "142km/h")

print(f"Rekisteritunnus: {auto.rekisteritunnus}")
print(f"Huippunopeus: {auto.huippunopeus}")
print(f"Tämänhetkinen_nopeus: {auto.tämänhetkinen_nopeus}")
print(f"Kuljettu_matka {auto.kuljettu_matka}")