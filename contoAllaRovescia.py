"""
Si prega di rispettare i termini della licenza: https://creativecommons.org/licenses/by/4.0/
"""

def contoallarovescia(n):
    if n <= 0:
        print("Via!")
    else:
        print(n)
        contoallarovescia(n-1)

num = int(input("Inserisci il numero di partenza:\n"))

print("Conto alla rovescia:")

contoallarovescia(num)