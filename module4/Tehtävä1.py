kuhan_pituus = float(input("Kalastaja kerro kuhan pituus senttimetreinä: "))
if kuhan_pituus < 37:
    print(f"Kuha on alamittainen, laske kuha takaisin järveen.\nAlimmasta saallitusta pyyntimitasta puuttuu {37-kuhan_pituus} cm.")
else:
    print("Kuha ei ole alamittainen.")    