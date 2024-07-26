"""Si prega di rispettare i termini della licenza: https://creativecommons.org/licenses/by/4.0/
"""
dizionario_persone = {}
codice_fiscale = ""

while codice_fiscale.lower() != "fine":
    codice_fiscale = input("Inserisci il codice fiscale (o 'fine' per terminare.): ")

    if codice_fiscale != 'fine':
        nome = input("Inserisci il nome: ")
        cognome = input("Inserisci il cognome: ")

        dizionario_persone[codice_fiscale] = {'nome': nome, 'cognome': cognome}
        print("Persona aggiunta con successo!\n")


# Stampa il dizionario risultante
print("Dizionario delle persone:")
for codice_fiscale, dati in dizionario_persone.items():
    print(f"Codice fiscale: {codice_fiscale}, Nome: {dati['nome']}, Cognome: {dati['cognome']}")

# Ricerca per codice fiscale
cerca = input("Inserisci il codice fiscale per ottenere nome e cognome: ")
trovato = False
for codice_fiscale, dati in dizionario_persone.items():
    if codice_fiscale == cerca:
        print(f"Il codice fiscale è di {dati['nome']} {dati['cognome']}")
        trovato = True
        break
if trovato != True:
    print("Il codice fiscale non è presente nel dizionario!")            
