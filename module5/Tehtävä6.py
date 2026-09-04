import random
arvottavien_pisteiden_määrä = int(input("Anna arvottavien pisteiden määrä: "))
pisteet = 0
pisteet_ympyrän_sisällä = 0
while pisteet <= arvottavien_pisteiden_määrä:
    pisteet += 1
    pisteen_x = random.uniform(-1, 1)
    pisteen_y = random.uniform(-1, 1)
    #x^2+y^2<1
    if pisteen_x ** 2 + pisteen_y ** 2 < 1:
        pisteet_ympyrän_sisällä += 1
else:
    piin_likiarvo = 4 * pisteet_ympyrän_sisällä / arvottavien_pisteiden_määrä
    print("piin likiarvo on:", piin_likiarvo)