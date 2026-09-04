while tuumat >= 0:
    tuumat = float(input("Anna tuumien määrä: "))
    if tuumat < 0:
        break
    tuumat_sentteinä = tuumat * 2.54
    print(f"{tuumat} tuumaa on {tuumat_sentteinä:.2f} senttimetriä.")
