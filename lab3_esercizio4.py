"""
Si prega di rispettare i termini della licenza: https://creativecommons.org/licenses/by-nc-sa/4.0/
"""

"""Esercizio 4: Leggere un numero, calcolare il fattoriale e stamparlo
"""

n = int(input("Inserisci un numero "))
fattoriale = 1

for i in range(1,n+1):
    fattoriale *= i
    # print(fattoriale) istruzione di stampa se voglio verificare ogni ciclo

print(fattoriale)