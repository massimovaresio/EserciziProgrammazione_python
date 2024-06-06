"""Questo modulo contiene esempi di codice correlati al libro:

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Sono stati rimossi i riferimenti al Copyright in quanto il seguente codice è stato modificato e rielaborato rispetto all'originale.

Si prega ugualmente di rispettare i termini della licenza: https://creativecommons.org/licenses/by/4.0/
"""

def al_contrario(parola1, parola2):
    """Funzione che confronta due parole e restituisce True quando una parola è scritta al contrario dell'altra.
    
    La prima istruzione if controlla se le parole sono della stessa lunghezza, altrimenti può subito restituire False.
    L'indice i attraversa parola1 in avanti mentre j attraversa parola2 a ritroso; se troviamo lettere che non coincino restituiamo False.
    Se invece il ciclo conclude normalmente possiamo restituire True.
    """      
    if len(parola1) != len(parola2):
        return False
    
    i = 0
    j = len(parola2) - 1

    while j >= 0: # include lo 0 per far sì che venga considerato anche il caso j[0]
        # se mi servisse un controllo di debug potrei fare la stampa print(i, j)
        if parola1[i] != parola2[j]:
            return False
        i = i + 1
        j = j - 1

    return True

def palindromo(parola):
    """Utilizzo la funzione al_contrario già definita per applicarla anche a palindromo.
    
    """ 
    return al_contrario(parola, parola)


p1 = input("Inserisci la prima parola: ")
p2 = input("Inserisci la seconda parola: ")

if al_contrario(p1, p2) == True:
    print("Le parole sono una il contrario dell'altra.")
else:
    print("Le parole non sono l'una il contrario dell'altra.")

print("-*" * 10) # riga per separazione

parola_palindromo = input("Inserisci la parola per verifica se è palindromo: ")

if al_contrario(parola_palindromo, parola_palindromo) == True:
    print("Sì, la parola è un palidromo.")
else:
     print("No, la parola non è un palidromo.")   

