"""Esercitazione sui dizionari

Creazione dizionario:
dizionario = {chiave1: valore1, chiave2: valore2}
dizionario = {} #creo un dizionario vuoto
la funzione dict() crea un dizionario vuoto
per aggiungere elementi (intesi come coppia chiave-valore) posso usare la notazione dizionario[chiave] = valore
ad esempio in un caso di strighe: dizionario['chiave'] = 'valore'
i dizionari supportano la funzione len() che restituisce il numero di elementi (coppie) che compongono il dizionario

Si prega di rispettare i termini della licenza: https://creativecommons.org/licenses/by-nc-sa/4.0/
"""

def istogramma(s):
    """Funzione istrogramma

    Input: stringa
    Output: dizionario con coppie di lettere associate ad un contatore

    La funzione riceve una stringa e per ogni lettera che la compone conta quante volte compare la lettera
    """
    dizionario = dict()
    for c in s:  # c sta per carattere o elemento della stringa
        if c == ' ': # gestisce il caso in cui ci siano spazi nella stringa e li salta non inserendoli nel dizionario
            continue         
        if c not in dizionario:
            dizionario[c] = 1
        else:
            dizionario[c] += 1
    return dizionario

# il ciclo for attraversa la stringa e ad ogni ripetizione, se il carattere c non compare nel dizionario lo aggiunge con chiave c e valore 1, se invece è già presente allora incrementa il valore di una unità

def stampa_isto(h): # dove h sta per un generico dizionario
    for chiave in sorted(h):   # sorted() è una funzione predefinita che ordina gli elementi del dizionario, che altrimenti hanno di default ordine imprevedibile
        print(chiave, h[chiave])

def inverti_dizionario(d):
    """Funzione per invertire un dizionario, 
    così che ogni coppia chiave-valore sia inverita rispetto al dizionario passato come argomento alla funzione

    ricorda che le liste possono essere usate come valori in un dizionario ma mai come chiavi, che devono essere sempre tipi immutabili
    ricorda anche che l'operatore in nei dizionari itera soltanto attraverso le chiavi
    """  
    inverso = dict()
    for chiave in d:
        valore = d[chiave]
        if valore not in inverso:
            inverso[valore] = [chiave]    # cioè se valore non è tra le chiavi di inverso, allora creo un nuovo elemento/coppia che ha come chiave il valore e come valore una lista, inizialmente di un solo elemento ma che poi incrementa a seconda delle frequenze
        else:
            inverso[valore].append(chiave) # se invece il valore è già presente come chiave, la chiave originale viene aggiunta alla lista associata a quel valore
    return inverso         


# ESECUZIONE
stringa = input("Inserisci la stringa desiderata: ")
isto = istogramma(stringa) # isto è un dizionario che viene creato attraverso la funzione istogramma(s)
print("Questo è il dizionario in formato predefinito:")
print(isto)
print("") # stampra riga di separazione
print("Questo è il dizionario visualizzato nel formato grafico voluto:")
stampa_isto(isto) # non uso il print esterno altrimenti alla fine mi darebbe anche un valore None dovuto al fatto che la funzione è vuota e non restitusce nulla, quindi di default restituisce None
print("") # stampra riga di separazione
isto_invertito = inverti_dizionario(isto)
print("Questo è il dizionario invertito:")
print(isto_invertito)
