"""
Si prega di rispettare i termini della licenza: https://creativecommons.org/licenses/by/4.0/
"""

def somma_nidificata(lista):
    somma = 0
    for i in lista:
        somma += i
    return somma    
    # Alternativamente al ciclo avrei potuto usare la funzione predefinita sum(lista)

t = [[1, 2], [3], [4, 5, 6]]
t1 = t[0]
t2 = t[1]
t3 = t[2]
nuova_lista = t1 + t2 + t3

print(somma_nidificata(nuova_lista))

"""
SOLUZIONE PROPOSTA NEL LIBRO:
def nested_sum(t):
    total = 0
    for nested in t:
        total += sum(nested)
    return total
"""

