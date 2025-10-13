def ackermann(m, n):
    """Calcola la funzione di Ackermann A(m, n)

    Vedi http://en.wikipedia.org/wiki/Ackermann_function

    n, m: non devono essere interi negativi
    """
    if m == 0:
        risultato = n + 1
    elif m > 0 and n == 0:
        risultato = ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        risultato = ackermann(m - 1, ackermann(m, n - 1))
    return risultato    


print(ackermann(3, 4))