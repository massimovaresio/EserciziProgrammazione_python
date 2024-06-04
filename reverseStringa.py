"""
Si prega di rispettare i termini della licenza: http://creativecommons.org/licenses/by/4.0/
"""

def reverseStringa(s):
    lunghezza = len(s)
    i = lunghezza - 1
    while i >= 0:
        lettera = s[i]
        print(lettera)
        i = i - 1

stringa = input("Inserisci la parola che verrà letta al contrario: ")
reverseStringa(stringa)       

