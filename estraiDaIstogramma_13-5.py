"""
Si prega di rispettare i termini della licenza: https://creativecommons.org/licenses/by-nc-sa/4.0/
"""

import random

def istogramma(t):
    """Funzione per creare istrogramma da una lista generica che viene passata

    Input: lista
    Output: dizionario contente i valori della lista e la loro frequenza di ripetizione

    La funzione riceve una lista e per ogni elemento che la compone conta quante volte compare l'elemento
    """
    d = dict()
    for i in t:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d

def estrai_da_isto(h):
    """
    Estrae un elemento dall'istogramma passto (in questo caso h) con probabilità proporzionale alla frequenza.

    Argomento/input:
        h (dict): Un dizionario che rappresenta l'istogramma, dove le chiavi sono
                     gli elementi e i valori sono le frequenze.

    Ritorno/output:
        Un elemento dell'istogramma, scelto con probabilità proporzionale alla frequenza.
    """
    # Estrai le chiavi (elementi) e i valori (frequenze) dal dizionario
    elementi = list(h.keys())
    frequenze = list(h.values())
    
    # Utilizza random.choices per estrarre un elemento in base alle frequenze
    elemento_estratto = random.choices(elementi, weights=frequenze, k=1) # ricorda che la funzione random.chioces restituisce una lista
    return elemento_estratto


lista = ['a', 'b', 'c', 'd', 'a', 'b']
isto = istogramma(lista)
print(isto)

# Esempio di utilizzo della funzione di estrazione
elemento = estrai_da_isto(isto)
print(elemento)  # Output come lista

# Accesso all'elemento della lista, se necessario
print(elemento[0])  # Output come singolo elemento della lista a cui accedo con l'indice
