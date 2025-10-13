def somma_cumulata(lista):
    somma = 0
    nuova_lista = []
    for i in lista:
        somma += i
        nuova_lista.append(somma)
    return nuova_lista    

t = [1, 2, 3]
print(somma_cumulata(t))

