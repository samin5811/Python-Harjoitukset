import math

kokonaisluku = int(input("Anna kokonaisluku: "))
if kokonaisluku == 1:
    print("Luku ei ole alkuluku")
elif kokonaisluku == 2:
    print("Luku on alkuluku")
elif kokonaisluku > 2 and kokonaisluku % 2 == 0:
    print("Luku ei ole alkuluku")
elif kokonaisluku > 2 and kokonaisluku % 2 != 0:
    kokonaisluvun_neliöjuuri = math.sqrt(kokonaisluku)
    for i in range(3, int(kokonaisluvun_neliöjuuri) + 1, 2):
        if kokonaisluku % i == 0:
            print("Luku ei ole alkuluku")
            break
    else: 
        print("Luku on alkuluku")
else:
    print("Luku ei ole alkuluku")
