def contoallarovescia(n):
    if n <= 0:
        print("Via!")
    else:
        print(n)
        contoallarovescia(n-1)

num = int(input("Inserisci il numero di partenza:\n"))

print("Conto alla rovescia:")

contoallarovescia(num)