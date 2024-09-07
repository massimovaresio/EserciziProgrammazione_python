"""
Si prega di rispettare i termini della licenza: https://creativecommons.org/licenses/by-nc-sa/4.0/
"""

def divisibili_per_tre(lista):
    """Prende una lista e genera due liste, una con i numeri divisibili per 3 e l'altra con i rimanenti

    input: lista in argomento

    output: tupla che contiene le due liste
    """
    t1 = []
    t2 = []

    # Itera attraverso gli elementi della lista passata in argomento
    for el in lista:
        if el % 3 == 0:
            t1.append(el)
        else:
            t2.append(el)

    return t1, t2


# Esecuzione
if __name__ == '__main__':
    lista_iniziale = [4, 1, 24, 3, 11, 5, 100]
    risultato = divisibili_per_tre(lista_iniziale)
    print("La tupla di liste risultante è la seguente:\n")    
    print(risultato)