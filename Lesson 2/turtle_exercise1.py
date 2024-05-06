'''Scrivete un programma che disegna un quadrato, un esagono, un ottagono, un
decagono. Tutti partendo dallo stesso punto, ma con colori diversi'''

import turtle

# Avviamo la finestra di lancio
window = turtle.Screen()

# Impostiamo il colore della finestra di gioco
backgroundColor = window.bgcolor("black")

turtleOne = turtle.Turtle()
turtleTwo = turtle.Turtle()
turtleThree = turtle.Turtle()

# dichiariamo i colori delle tartarughe
turtleOneColor = turtleOne.color("blue")
turtleTwoColor = turtleTwo.color("red")
turtleThreeColor = turtleThree.color("green")

# Chiediamo alla tartaruga 1 di disegnare un esagono:

for _ in range(6):
    turtleOne.forward(100)
    turtleOne.left(60)

# Chiediamo alla tartaruga 2 di disegnare un ottagono:

for _ in range(8):
    turtleTwo.forward(100)
    turtleTwo.left(45)

# Chiediamo alla tartaruga 3 di disegnare un decagono:

for _ in range(10):
    turtleThree.forward(100)
    turtleThree.left(36)
    
# Teniamo la finestra del programma aperta
window.mainloop()