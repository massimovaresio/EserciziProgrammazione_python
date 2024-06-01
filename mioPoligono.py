import turtle

bob = turtle.Turtle()

print(bob)

# Disegna un quadrato
for i in range(4):
    bob.fd(100)
    bob.lt(90)

turtle.mainloop()
