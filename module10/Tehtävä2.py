class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, kerros):
        if self.alin_kerros <= kerros <= self.ylin_kerros:
            while kerros != self.nykyinen_kerros:
                if kerros < self.nykyinen_kerros:
                    self.kerros_alas()
                else:
                    self.kerros_ylös()

    def kerros_ylös(self):
        self.nykyinen_kerros += 1
        print(f"{self.nykyinen_kerros} kerros")

    def kerros_alas(self):
        self.nykyinen_kerros -= 1
        print(f"{self.nykyinen_kerros} kerros")

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_määrä):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissien_määrä = hissien_määrä
        self.hissit = []
        for i in range(hissien_määrä):
            hissi = Hissi(alin_kerros, ylin_kerros)
            self.hissit.append(hissi)
    def aja_hissiä(self, hissin_numero, kerros):
        self.hissit[hissin_numero].siirry_kerrokseen(kerros)

talo = Talo(0, 5, 5)
talo.aja_hissiä(1, 5)
print("")
talo.aja_hissiä(2, 5)
print("")
talo.aja_hissiä(1, 2)
print("")
talo.aja_hissiä(2, 1)
