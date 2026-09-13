def gallonat_litroiksi(gallonat):
    gallonat_litroina = gallonat * gallona_litroina
    return gallonat_litroina

gallona_litroina = 3.758
gallonat = 0
while gallonat >= 0:
    gallonat = float(input("Anna gallonamäärä: "))
    gallonat_litroina = gallonat_litroiksi(gallonat)
    print(f"{gallonat} gallonaa on {gallonat_litroina:.2f} litraa.")