"""Si prega di rispettare i termini della licenza: https://creativecommons.org/licenses/by-nc-sa/4.0/

    RICHIESTA: scrivere una funzione che prende come parametro una lista e mette in una tupla gli elementi in
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


"""Soluzione alternativa che usa la funzione enumerate() che permette di attraversare gli elementi
   di una lista e i loro indici. Il risultato è un oggetto enumerate, che itera una sequenza di coppie
 
def dividiPariDispari_enum(lista):
    
    t = tuple()
    t_temp = list()
    s = list()

    # Itera attraverso gli elementi della lista passata in argomento
    for indice, elemento in enumerate(lista):
        if indice % 2 == 0:
            t_temp.append(elemento)
        else:
            s.append(elemento)

    t = tuple(t_temp)

    print("Questa è la tupla con gli elementi pari: ", t)
    print("Questa è la lista con gli elementi dispari: ", s)

"""


lista_iniziale = [8, 1, 3, 4, 2, 6, 5]
dividiPariDispari(lista_iniziale)
# dividiPariDispari_enum(lista_iniziale)

