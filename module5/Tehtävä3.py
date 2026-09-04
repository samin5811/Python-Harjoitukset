luku = float(input("Anna luku: "))
pienin_luku = luku
isoin_luku = luku
while True:
    luku = (input("Anna luku: "))
    if luku == "":
        print(f"isoin luku = {isoin_luku}")
        print(f"pienin luku = {pienin_luku}")
        break   
    luku = float(luku)
    if luku >= isoin_luku:
        isoin_luku = luku
    if luku <= pienin_luku:
        pienin_luku = luku 
    