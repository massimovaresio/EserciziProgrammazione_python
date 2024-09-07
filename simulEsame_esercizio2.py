"""Si prega di rispettare i termini della licenza: https://creativecommons.org/licenses/by-nc-sa/4.0/

    RICHIESTA: scrivere una funzione che prende come parametro una lista di tuple. Nella funzione creare un
    dizionario dove, per ogni elemento della lista, la chiave del dizionario è il primo elemento della tupla
    e il valore è una tupla di due elementi: il primo elemento è la posizione che la tupla aveva nella
    lista e il secondo è l'elemento in seconda posizione nella tupla di partenza. Restituire il dizionario
    al chiamante che lo stampa.

    APPROCCIO UTILIZZATO: dopo avere creato una versione di prova, ho preferito implementare il codice con
    l'ausilio della funzione enumerate() in quanto rende il codice più sintetico e risulta più intuitivo e
    semplice sia in lettura che in esecuzione.
"""

"""VERSIONE ALTERNATIVA SENZA USO DELLA FUNZIONE PREDEFINITA enumerate()
    
    def crea_dizionario(lista_di_tuple):

    dizionario = dict()

    for i in range(len(lista_di_tuple)):
        t = lista_di_tuple[i]  #crea una tupla t che rappresenta ciascun elemento della lista di tuple
        chiave = t[0]
        valore = (i, t[1])
        dizionario[chiave] = valore

    return dizionario
"""

def crea_dizionario_enum(lista_di_tuple):
    """Crea un dizionario secondo le specifiche della richiesta

    argomento: lista di tuple
    output: nuovo dizionario
    """

    dizionario = dict()

    for indice, elemento in enumerate(lista_di_tuple):  #la funzione enumerate() permette di iterare contemporaneamente indice ed elementi di una sequenza
        chiave = elemento[0]
        valore = (indice, elemento[1])
        dizionario[chiave] = valore

    return dizionario


def stampa_dizionario(dizionario):
    """Stampa il dizionario che viene passato in argomento con vista migliorata
    """
    for chiave, valore in dizionario.items():
        print(f"{chiave}: {valore}")





# ESECUZIONE
if __name__ == '__main__':
    lista_iniziale = [('A', 'ciao'), ('B', 'come'), ('C', 'va')]
    nuovo_diz = crea_dizionario_enum(lista_iniziale)
    stampa_dizionario(nuovo_diz)


