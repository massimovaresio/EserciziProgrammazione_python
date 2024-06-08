
"""
Si prega di rispettare i termini della licenza: https://creativecommons.org/licenses/by/4.0/
"""

memo = {0:0, 1:1} # dizionario di partenza con i valori di fibonacci(0) e fibonacci(1)

def fibonacci(n):
    """Calcola la funzione di Fibonacci con l'aggiunta della memoizzazione con un dizionario

    fibonacci(0) = 0
    fibonacci(1) = 1
    fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)
    
    """
    if n in memo:      # n viene iterato tra le chiavi
        return memo[n]

    result = fibonacci(n - 1) + fibonacci(n - 2)
    memo[n] = result
    return result


num = int(input("Inserisci un numero intero positivo: "))

print(fibonacci(num))