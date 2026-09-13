def nopan_heitto():
    import random
    random_luku = random.randint(1, 6)
    return random_luku
luku = 0
while luku != 6:
    luku = nopan_heitto()
    print(luku)
