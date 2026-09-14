nimet = set()

nimi = "random"

while nimi != "":
    nimi = input("Anna nimi: ")
    if nimi == "":
        continue
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        
    nimet.add(nimi)    
else:
    print(nimet)    