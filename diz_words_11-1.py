"""
Si prega ugualmente di rispettare i termini della licenza: https://creativecommons.org/licenses/by-nc-sa/4.0/
"""

def crea_diz(file):
    d = dict()
    for riga in file:
        parola = riga.strip()
        d[parola] = 'valore'
    return d

def stampa_diz(d):
    for chiave in sorted(d):
        print(chiave, d[chiave])

def verifica(str):
    if str in dizionario:
        return True
    else:
        return False        


# Apri il file 'words.txt' in modalità lettura
fin = open('words.txt')

dizionario = crea_diz(fin)
stampa_diz(dizionario)

# Chiudi manualmente il file
fin.close()

print("Inserisci una parola per verificare se la stringa è presente nel dizionario.")
parola_inserita = input("Scrivi la stringa da verificare: ")

if verifica(parola_inserita) == True:
    print(f"La parola '{parola_inserita}' è presente nel dizionario.")
else:
    print(f"La parola '{parola_inserita}' non è presente nel dizionario.") 

