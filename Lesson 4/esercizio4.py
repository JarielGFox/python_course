import turtle

# Avvio la finestra di lancio
window = turtle.Screen()

# Impostiamo il colore nero di bg
window.bgcolor("black")

# Istanziamo una tartaruga
squirtle = turtle.Turtle()

# Diamo un colore a squirtle
def colorChange(colore = str(input('Inserisci un colore: '))):
    squirtle.color(colore)

# Diamo una velocità a squirtle
squirtle.speed(1)

# Mostriamo un messaggio nel programma per informare l'utente di controllare il terminale
squirtle.write('Controlla il terminale!', True, align="left", font=("Arial", 16, "normal"))
turtle.ontimer(squirtle.clear, 2500)

# Chiediamo all'utente la lunghezza lato del poligono
userQuestion = input("Inserisci la lunghezza lato del poligono: ")

# Invochiamo la funzione per il cambio del colore:
colorChange()

def drawSquare():
    for _ in range(4):
        squirtle.forward(100)
        squirtle.left(90)
def drawTriangle():
    for _ in range(3):
        squirtle.forward(100)
        squirtle.left(120)
        
        
if int(userQuestion) % 2 == 0:
    drawSquare()
else:
    drawTriangle()
        
        
if int(userQuestion) % 2 == 0:
    squirtle.penup()
    squirtle.setx(-200)
    squirtle.pendown()
    squirtle.write('Ecco a te un quadrato!', True, align="left", font=("Arial", 16, "normal"))
else:
    squirtle.penup()
    squirtle.setx(-200)
    squirtle.pendown()
    squirtle.write('Ecco a te un triangolo!', True, align="left", font=("Arial", 16, "normal"))

# Manteniamo aperta la finestra di gioco
window.mainloop()

