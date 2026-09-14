kuukauden_numero = int(input("Anna kuukauden numero : "))

vuodenajat = ("kevät", "kesä", "syksy", "talvi")

if 3 <= kuukauden_numero <= 5:
    vuodenaika = vuodenajat[0]
elif 6 <= kuukauden_numero <= 8:
    vuodenaika = vuodenajat[1]
elif 9 <= kuukauden_numero <= 11:
    vuodenaika = vuodenajat[2]
elif 1 <= kuukauden_numero <= 2 or kuukauden_numero == 12:
    vuodenaika = vuodenajat[3]
else:
    vuodenaika = "väärä kuukauden numero"    

print(f"kuukauden {kuukauden_numero} vuodenaika on {vuodenaika}")

## Toinen tapa

kuukauden_numero = int(input("Anna kuukauden numero : "))

vuodenajat = ("Talvi", "Talvi", "Kevät", "Kevät", "Kevät", "Kesä", "Kesä", "Kesä", "Syksy", "Syksy", "Syksy", "Talvi")

print(f"kuukauden {kuukauden_numero} vuodenaika on {vuodenajat[kuukauden_numero - 1]}")