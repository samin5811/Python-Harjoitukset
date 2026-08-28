suorakulmion_kanta = float(input("Anna suorakulmion kanta: "))
suorakulmion_korkeus = float(input("Anna suorakulmion korkeus: "))

suorakulmion_pinta_ala = suorakulmion_kanta * suorakulmion_korkeus
suorakulmion_piiri = suorakulmion_kanta * 2 + suorakulmion_korkeus * 2

print("Suorakulmion pinta-ala = " + str(suorakulmion_pinta_ala))
print("Suorakulmion piiri = " + str(suorakulmion_piiri))