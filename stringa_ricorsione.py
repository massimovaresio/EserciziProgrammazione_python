"""
Si prega di rispettare i termini della licenza: https://creativecommons.org/licenses/by-nc-sa/4.0/
"""

def stampa_n_volte(s, n):
    if n <= 0:
        return
    else:
        print(s)
        stampa_n_volte(s, n-1)

stringa = input("Inserisci la stringa: ")
numero = int(input("Inserisci il numero di volte: "))

stampa_n_volte(stringa, numero)