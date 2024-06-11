
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
    testo_libro = open(nomefile, encoding='utf-8')  # specifico la codifica del file per evitare errori nella lettura
    # Salta le prime 30 righe dell'intestazione
    # '_' come variabile di iterazione, segnalo che questa variabile non sarà utilizzata nel corpo del ciclo; è una convenzione comune in Python per indicare che la variabile non ha importanza; se avessi usato anche qui 'riga' comunque funzionava
    for _ in range(30):
            next(testo_libro)
        
    # Elabora le righe rimanenti
    for riga in testo_libro:
        elabora_riga(riga, isto)
    testo_libro.close()    
    return isto


def elabora_riga(riga, isto):
    """Per ogni riga separa le parole, scarta spazi e punteggiatura e converti tutto il lettere minuscole
    """
    riga = riga.replace('-', ' ')  # metodo delle stringhe replace vedi docs https://docs.python.org/3/library/stdtypes.html#string-methods

    for parola in riga.split():  # suddivide la riga in una lista di stringhe
        parola = parola.strip(string.punctuation + string.whitespace)  # rimozione della punteggiatura e degli spazi
        parola = parola.lower()  # converti tutto in lettere minuscole (in realtà vrea una nuova stringa dato che sono immutabili)
        isto[parola] = isto.get(parola, 0) + 1  # crea un nuovo elemento nell'istogramma o incrementa uno esistente


def parole_totali(isto):
     """Conta il numero di parole totali aggiungendo le frequenze dell'istogramma
     """
     return sum(isto.values())


def parole_diverse(isto):
     """Conta il numero di parole diverse contando semplicemente il numero di elementi nel dizionario
     """
     return len(isto)


# ESECUZIONE
istogramma = elabora_file('emma.txt')

# Conta parole totali e stampa risultato
print("Numero totale di parole: ", parole_totali(istogramma))

# Conta parole diverse e stampa il risultato
print("Numero di parole diverse: ", parole_diverse(istogramma))
