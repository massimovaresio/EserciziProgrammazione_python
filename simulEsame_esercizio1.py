"""Si prega di rispettare i termini della licenza: https://creativecommons.org/licenses/by/4.0/

    RICHIESTA: Scrivere una funzione che prende come parametro una lista e mette in una tupla gli elementi in
    posizione pari e in un'altra lista gli elementi in posizione dispari. Al termine stampa la lista
    risultante e la tupla risultante.
"""

def dividiPariDispari(lista):
    t = tuple()
    t_temp = list()
    s = list()

    # Itera attraverso gli elementi della lista passata in argomento
    for i in range(len(lista)):
        if i % 2 == 0:
            t_temp.append(lista[i])
        else:
            s.append(lista[i])

    t = tuple(t_temp)

    print("Questa è la tupla con gli elementi pari: ", t)
    print("Questa è la lista con gli elementi dispari: ", s)


lista_iniziale = [8, 1, 3, 4, 2, 6, 5]
dividiPariDispari(lista_iniziale)   
