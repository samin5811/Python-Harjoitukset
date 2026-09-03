sukupuoli = input("Anna biologinen sukupuoli (mies/nainen): ")
hemoglobiiniarvo = float(input("Anna hemoglobiiniarvo (g/l): "))
if sukupuoli == "nainen":
    if hemoglobiiniarvo < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemoglobiiniarvo > 175:
        print("Hemoglobiiniarvo on korkea.")
    else:
        print("Hemoglobiiniarvo on normaali.")
elif sukupuoli == "mies":
    if hemoglobiiniarvo < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemoglobiiniarvo > 195:
        print("Hemoglobiiniarvo on korkea.")
    else:
        print("Hemoglobiiniarvo on normaali.")
else:
    print("Virheellinen sukupuoli. Anna 'mies' tai 'nainen'.")        