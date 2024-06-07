"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: https://creativecommons.org/licenses/by/4.0/
"""

def is_triple_double(word):
    """Tests if a word contains three consecutive double letters.
    
    word: string

    returns: bool
    """
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2  # Avanza di due posizioni, saltando la doppia già contata. Questo codice viene eseguito solo se il controllo precedente (if count == 3:) non ha restituito True
        else:
            i = i + 1 - 2*count
            count = 0
            """
            Se non trova una coppia, l'algoritmo deve "riposizionarsi" per ricominciare la ricerca di coppie consecutive da una posizione precedente, 
            considerando quante coppie ha già trovato. Questo riposizionamento è fatto con la linea i = i + 1 - 2*count.
            La funzione continua così, ricominciando la ricerca ogni volta che non trova una coppia di lettere doppie consecutive, 
            fino a trovare tre coppie consecutive o fino alla fine della parola.
            La linea i = i + 1 - 2*count è progettata per riposizionare l'indice i in modo che possa ricominciare la ricerca delle coppie consecutive 
            di lettere doppie senza perdere possibili combinazioni. Questo meccanismo permette di gestire interruzioni tra coppie consecutive 
            e assicura che la funzione controlli accuratamente ogni possibile tripla coppia di lettere doppie.
            """
    return False # Se il ciclo termina senza trovare tre coppie consecutive di lettere doppie, restituisce False


def find_triple_double():
    """Reads a word list and prints words with triple double letters."""
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print(word)


print('Here are all the words in the list that have')
print('three consecutive double letters.')
find_triple_double()
print('')


"""
**COMMENTO SULL'USO DI UN CICLO WHILE PIUTTOSTO CHE UN CICLO FOR

Il ciclo while è utile quando vuoi un controllo più fine su come l'indice i viene incrementato all'interno del ciclo, 
specialmente quando i può essere incrementato di più di 1 in alcuni casi o riportato indietro in altri.
Con un ciclo for, possiamo ancora controllare l'indice i manualmente all'interno del ciclo. Tuttavia, il ciclo for tradizionale in Python incrementa automaticamente i ad ogni iterazione, 
quindi dobbiamo gestire manualmente il salto delle iterazioni quando troviamo coppie consecutive di lettere doppie.

def is_triple_double(word):
    count = 0
    i = 0  # L'indice i sarà incrementato manualmente
    for _ in range(len(word) - 1):  # Usiamo _ perché non ci serve l'indice del ciclo `for`
        if i >= len(word) - 1:
            break  # Esci dal ciclo se l'indice i supera la lunghezza della parola meno 1
        
        if word[i] == word[i + 1]:
            count += 1
            if count == 3:
                return True
            i += 2  # Salta alla prossima coppia
        else:
            i = i + 1 - 2 * count
            count = 0
    return False

L'uso del ciclo for è possibile, ma richiede una gestione più attenta dell'indice i. In un ciclo for, 
devi essere consapevole del fatto che l'indice è incrementato automaticamente ad ogni iterazione, 
il che può complicare il controllo manuale dell'indice come nel tuo caso. Il ciclo while offre una maggiore flessibilità per questo
tipo di gestione manuale dell'indice.

In generale, se il controllo dell'indice è cruciale e può essere complesso, un ciclo while è spesso la scelta più diretta e leggibile.
    
"""