
"""
Si prega di rispettare i termini della licenza: http://creativecommons.org/licenses/by/4.0/
"""

def fibonacci(n):
    """Calcola la funzione di Fibonacci

    fibonacci(0) = 0
    fibonacci(1) = 1
    fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)
    
    """
    if n == 0:   # caso base
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)   


num = int(input("Inserisci un numero intero positivo: "))

print(fibonacci(num))