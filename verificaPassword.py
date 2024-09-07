"""Si prega di rispettare i termini della licenza: https://creativecommons.org/licenses/by-nc-sa/4.0/
"""

"""RICHIESTA:
Scrivere una funzione che prende una stringa in input e controlla che sia una buona password:
# Almeno 8 caratteri, almeno un numero, almeno una lettera maiuscola, almeno una minuscola
# e almeno un carattere speciale.
# Se tutti i criteri sono rispettati, ritorna la stringa "Password forte"
# Altrimenti ritorna la stringa "Password debole" 
# Usare gli opportuni metodi consultando la documentazione
"""

import string

def controllo_password(password):
    controllo_lunghezza = False
    controllo_numero = False
    controllo_maiuscola = False
    controllo_minuscola = False
    controllo_speciale = False

    if len(password) < 8:
        controllo_lunghezza
    else:
        controllo_lunghezza = True
        for c in password:
            if c in string.ascii_lowercase:
                controllo_minuscola = True
            if c in string.ascii_uppercase:
                controllo_maiuscola = True
            if c in string.digits:
                controllo_numero = True
            if c in string.punctuation:
                controllo_speciale = True

    if controllo_lunghezza and controllo_numero and controllo_maiuscola and controllo_minuscola and controllo_speciale:
        risultato = "Password forte"
    else:
        risultato = "Password debole"

    return risultato


# Esecuzione
if __name__ == '__main__':
    prova = input("Inserisci un password da verificare: ")
    print(controllo_password(prova))
    
