"""Questo modulo contiene esempi di codice correlati al libro:

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Sono stati rimossi i riferimenti al Copyright in quanto il seguente codice è stato modificato e rielaborato rispetto all'originale.

Si prega ugualmente di rispettare i termini della licenza: https://creativecommons.org/licenses/by-nc-sa/4.0/
"""

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

