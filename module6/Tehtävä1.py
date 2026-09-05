import random
noppien_määrä = int(input("Anna noppien määrä: "))
for noppa in range(noppien_määrä):
    print(random.randint(1, 6))