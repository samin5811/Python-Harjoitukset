def lista_ilman_parittomia(numero_lista):
    luku_lista = []
    for numero in numero_lista:
        luku_lista.append(numero)
        if numero % 2 != 0:
            luku_lista.remove(numero)
    return luku_lista

numero_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
numero_lista_ilman_parittomia = lista_ilman_parittomia(numero_lista)
print(numero_lista)
print(numero_lista_ilman_parittomia)