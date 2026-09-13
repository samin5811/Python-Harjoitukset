def nopan_heitto(nopan_maksimiluku):
    import random
    random_luku = random.randint(1, nopan_maksimiluku)
    return random_luku
luku = 0
nopan_maksimiluku = int(input("Anna nopan isoin luku: "))
while luku != nopan_maksimiluku:
    luku = nopan_heitto(nopan_maksimiluku)
    print(luku)