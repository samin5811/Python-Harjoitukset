import random
noppien_määrä = int(input("Anna noppien määrä: "))
noppien_summa = 0
for noppa in range(noppien_määrä):
    noppaluku = random.randint(1, 6)
    print(noppaluku)
    noppien_summa += noppaluku
print(f"summa: {noppien_summa}")