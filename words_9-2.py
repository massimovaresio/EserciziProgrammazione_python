def niente_e(parola):
    for lettera in parola:
        if lettera == 'e':
            return False
    return True

# Apri il file 'words.txt' in modalità lettura
fin = open('words.txt')

for riga in fin:
    parola = riga.strip()  # Rimuovi eventuali spazi bianchi iniziali/finali
    if niente_e(parola):
        print(parola)

# Chiudi manualmente il file
fin.close()

