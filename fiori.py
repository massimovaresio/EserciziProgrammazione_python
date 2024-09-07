
"""Questo modulo contiene esempi di codice correlati al libro:

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Sono stati rimossi i riferimenti al Copyright in quanto il seguente codice è stato modificato e rielaborato rispetto all'originale.

Si prega ugualmente di rispettare i termini della licenza: https://creativecommons.org/licenses/by-nc-sa/4.0/
"""

import turtle  # Documentazione del modulo Turtle graphics: https://docs.python.org/3/library/turtle.html#module-turtle
import math


def polilinea(t, n, lunghezza, angolo):
    """Disegna un segmento con n linee.

    t: oggetto tartaruga (Turtle)
    n: numero di linee del segmento
    lunghezza: lunghezza di ogni segmento
    angolo: gradi dell'angolo tra i segmenti
    """
    for i in range(n):
        t.fd(lunghezza)
        t.lt(angolo)


def arco(t, r, angolo):
    """Disegno un arco dato un certo raggio e angolo.

    t: oggetto tartaruga (Turtle)
    r: raggio
    angolo: angolo sotteso dall'arco, in gradi
    """
    lunghezza_arco = 2 * math.pi * r * abs(angolo) / 360
    n = int(lunghezza_arco / 4) + 3
    passo_lunghezza = lunghezza_arco / n
    passo_angolo = float(angolo) / n

    # effettuare una leggera virata a sinistra prima di partire riduce l'errore causato dall'approssimazione dell'arco
    t.lt(passo_angolo / 2)
    polilinea(t, n, passo_lunghezza, passo_angolo)
    t.rt(passo_angolo / 2)


def petalo(t, r, angolo):
    """Disegna un petaloo usando due archi.

    t: oggetto tartaruga (Turtle)
    r: raggio dell'arco
    angolo: angolo (gradi) che sottende l'arco
    """
    for i in range(2):
        arco(t, r, angolo)
        t.lt(180-angolo)


def fiore(t, n, r, angolo):
    """Disegna un fiore con n petali.

    t: oggetto tartaruga (Turtle)
    n: numero di petaloi del fiore
    r: raggio dell'arco
    angolo: angolo (gradi) che sottende l'arco
    """
    for i in range(n):
        petalo(t, r, angolo)
        t.lt(360.0/n)


def muovi(t, lunghezza):
    """muovi la tartaruga (t) in avanti (lunghezza) senza lasciare il percorso.
    Lascia la penna.
    """
    t.pu()
    t.fd(lunghezza)
    t.pd()


bob = turtle.Turtle()

# Disegna una sequenza di fiori.
muovi(bob, -100)
fiore(bob, 7, 60.0, 60.0)

muovi(bob, 100)
fiore(bob, 10, 40.0, 80.0)

muovi(bob, 100)
fiore(bob, 20, 140.0, 20.0)

bob.hideturtle()
turtle.mainloop()