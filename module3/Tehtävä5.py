leiviskät = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

leiviskät_nauloina = leiviskät * 20
naulat_luoteina = (naulat + leiviskät_nauloina) * 32
luodit_grammoina = (luodit + naulat_luoteina) * 13.3
grammat_kiloina = luodit_grammoina / 1000

print(f"\n {int(grammat_kiloina)} kilogrammaa ja {luodit_grammoina % 1000:.2f} grammaa")