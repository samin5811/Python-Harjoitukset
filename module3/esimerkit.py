# Muuttujat ja vuorovaikutteiset ohjelmat
# Tää on kommentti
##username = input("Syötä käyttäjätunnuksesi: ")
##username = "Tino"

##väri_input = input("Syötä lempivärisi: ")

# CRTL + Z

##print("Huomenta " + username + "!")
##print("vääri väri---> " + väri_input)
##print("Huomenta!\nTämä on esimerkkiohjelma.")
##print('"Kaikille"')

# CTRL + S

eka = -9
toka = 12_456_123_180
kolmas = 4.973
neljäs = -4 + 2j

##print(eka)
##print(toka)
##print(kolmas)
##print(neljäs)
##print(neljäs.real)
##print(neljäs.imag)

nimi = "Petra"  # Kaksinkertaisilla lainausmerkeillä
tervehdys = 'Hei maailma!'  # Yksinkertaisilla lainausmerkeillä
luku_tekstina = "12345"  # Vaikka sisältää numeroita, se on tekstiä, koska on lainausmerkkien sisällä
tyhja_merkkijono = ""  # Tyhjä merkkijono
lause1 = "Bob sanoi: 'Hei!'"  # Kaksinkertaiset lainausmerkit, yksinkertaiset osa merkkijonoa
lause2 = 'Bob vastasi: "Moi!"'  # Yksinkertaiset lainausmerkit, kaksinkertaiset osa merkkijonoa
##print()
##print(nimi)
##print(tervehdys)
##print(luku_tekstina)
##print(tyhja_merkkijono)
##print(lause1)
##print(lause2)
##print("fahrenheit to celsius converter")
temperature = input("Give temperature in fahrenheit: ")
celsius = (int(temperature) - 32) * 5 / 9
##print("Conversion result: " + str(celsius))

# CTRL + K + C
# CRTL + K + U

print(f"Fahrenheit {float(temperature):.2f} = Lämpötila Celsius-asteina: {celsius:6.2f}")
print("\n")

import math

pii_luku = math.pi

print(f"{'Pii':12s}:{math.pi:10.5f}")
print(f"{'Neperin luku':12s}:{math.e:10.5f}")