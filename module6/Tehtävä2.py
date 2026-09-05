luvut = []
luku = 0
while luku != "" or len(luvut) < 5:
    luku = (input("Anna luku: "))
    if luku == "":
        if len(luvut) < 5:
            print("Anna lisää lukuja")
        continue
    else:
        luvut.append(float(luku))
else:
    luvut.sort(reverse=True)
    for n in range(5):
        print(luvut[n])