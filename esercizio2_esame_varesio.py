"""
Si prega di rispettare i termini della licenza: https://creativecommons.org/licenses/by-nc-sa/4.0/
"""

def crea_dizionario(tupla_liste):
    # Dividi la tupla in due liste
    lista1, lista2 = tupla_liste
    
    # Verifica che le due liste abbiano la stessa lunghezza
    if len(lista1) != len(lista2):
        print("Le due liste devono avere lo stesso numero di elementi.")
        raise ValueError("Le due liste devono avere lo stesso numero di elementi.")
    
    lunghezza = len(lista1)
    
    # Crea il dizionario
    dizionario = {}

    for i in range(lunghezza):
        # La chiave è l'elemento della prima lista
        # Il valore è una tupla data dall'indice i e dall'elemento corrispondente
        chiave = lista1[i]
        elemento = lista2[i]
        valore = (i, elemento)
        dizionario[chiave] = valore
    
    return dizionario


def stampa_in_colonna(dizionario):
    print("Dizionario con vista a colonne:")
    for chiave, valore in dizionario.items():
        print(f"{chiave}: {valore}")


"""versione prova con funzione enumerate()

def crea_dizionario(tupla_liste):
    # Dividi la tupla in due liste
    lista1, lista2 = tupla_liste
    
    # Crea il dizionario
    dizionario = {}
    for indice, elemento in enumerate(lista1):
        chiave = elemento
        valore = (indice, lista2[indice])
        dizionario[chiave] = valore
    
    return dizionario
"""    

# Esecuzione
if __name__ == '__main__':
    tupla_iniziale = (["Primo", "Secondo", "Terzo"], ["a", "b", "c"])
    risultato = crea_dizionario(tupla_iniziale)
    print(risultato)

    stampa_in_colonna(risultato)