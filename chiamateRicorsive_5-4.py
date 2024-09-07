"""
Si prega di rispettare i termini della licenza: https://creativecommons.org/licenses/by-nc-sa/4.0/
"""

def ricorsione(n, s):
    """Dati due numeri interi, chiama ricorsivamente fino a raggiungere il caso base n == 0 e stampa i passaggi come
       se fosse rappresentato un diagramma di stack; infine stampa s quando raggiunge il caso base 

    Argomenti: n e s sono due numeri interi
    """
    if n == 0:
        print(s)
    else:
        print("Numeri passati: ", n, s, "- Dopo chiamata ricorsione: ", n-1, n+s)  # Istruzione di stampa per capire i passaggi, come diagramma di stack 
        ricorsione(n-1, n+s)


ricorsione(3, 0) 

# ricorsione(-1, 0) se faccio questa chiamata ho ricorsione infinita perché non raggiungo mai il caso base n == 0