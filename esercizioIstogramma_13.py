
"""Questo modulo contiene esempi di codice correlati al libro:

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Sono stati rimossi i riferimenti al Copyright in quanto il seguente codice è stato modificato e rielaborato rispetto all'originale.

Si prega ugualmente di rispettare i termini della licenza: https://creativecommons.org/licenses/by/4.0/
"""

# OBIETTIVO: progettare un programma che legge un file di testo e costruisce un istogramma delle parole contenute e poi esegue altre operazioni

import string

def elabora_file(nomefile):
    """Riceve come argomento un file e crea un istogramma di parole
    """
    isto = dict()
    testo_libro = open(nomefile)
    for riga in testo_libro:
        elabora_riga(riga, isto)
    return isto

def elabora_riga(riga, isto):
    """Per ogni riga separa le parole, scarta spazi e punteggiatura e converti tutto il lettere minuscole
    """
    riga.replace('-', ' ')  # metodo delle stringhe replace vedi docs https://docs.python.org/3/library/stdtypes.html#string-methods

    for parola in riga.split():
        parola = parola.strip(string.punctuation + string.whitespace)
        parola = parola.lower()
        isto[parola] = isto.get(parola, 0) + 1


# ESECUZIONE
istogramma = elabora_file('words.txt')
print(istogramma)      