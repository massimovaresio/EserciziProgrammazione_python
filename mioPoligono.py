import turtle

bob = turtle.Turtle()

print(bob)

"""
# Disegna un quadrato; istruzione semplice con ciclo

for i in range(4):
    bob.fd(100)
    bob.lt(90)

"""

"""
# Esempio riproposto con opzione di incapsulamento in una funzione quadrato()

def quadrato(t)
    for i in range(4):
        bob.fd(100)
        bob.lt(90)

quadrato(bob)        

"""

# Esempio riprosto con opzione di generalizzazione della funzione; così è possibile dare al quadrato dimensione a piacere cambiando il parametro 'lunghezza'

def quadrato(t, lunghezza):
    for i in range(4):
        t.fd(lunghezza)
        t.lt(90)

quadrato(bob, 100)

turtle.mainloop()
