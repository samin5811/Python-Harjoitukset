käyttäjätunnus = "python"
salasana = "rules"
väärä_input_määrä = 0
while True:
    käyttäjätunnus_input = input("Anna käyttäjätunnus: ")
    salasana_input = input("Anna salasana: ")
    if käyttäjätunnus_input == käyttäjätunnus and salasana_input == salasana:
        print("Tervetuloa!")
        break
    else:
        print("Pääsy evätty.")
        väärä_input_määrä += 1
        if väärä_input_määrä >= 5:
            break