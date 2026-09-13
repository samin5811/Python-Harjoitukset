def listan_lukujen_summa(numero_lista):
    summa = 0
    for numero in numero_lista:
        summa += numero
    return summa

numero_lista = [1, 2, 3, 4, 5]
numeroiden_summa = listan_lukujen_summa(numero_lista)
print(numeroiden_summa)