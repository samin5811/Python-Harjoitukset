numero1 = float(input("Anna ensimmäinen numero: "))
numero2 = float(input("Anna toinen numero: "))
numero3 = float(input("Anna kolmas numero: "))

numeroiden_summa = numero1 + numero2 + numero3
numeroiden_tulo = numero1 * numero2 * numero3
numeroiden_keskiarvo = numeroiden_summa / 3

print(f"\nNumeroiden summa = {numeroiden_summa:.2f}")
print(f"Numeroiden tulo = {numeroiden_tulo:.2f}")
print(f"Numeroiden keskiarvo = {numeroiden_keskiarvo:.2f}")