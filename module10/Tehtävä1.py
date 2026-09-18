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

alin_kerros = 0
ylin_kerros = 10
h = Hissi(alin_kerros, ylin_kerros)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(alin_kerros)