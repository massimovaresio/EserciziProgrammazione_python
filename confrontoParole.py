"""
Si prega di rispettare i termini della licenza: https://creativecommons.org/licenses/by/4.0/
"""

def in_entrambe(parola1, parola2):
    for lettera in parola1:
        if lettera in parola2:
            print(lettera)

prima_parola = input("Inserisci la prima parola: ")
seconda_parola = input("Inserisci la seconda parola: ")
in_entrambe(prima_parola, seconda_parola)


