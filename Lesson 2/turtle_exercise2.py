'''Semplificate il turtle_program per disegnare 2 quadrati e 2 trinagoli con 4
tartarughe..utilzzando i loop for'''

# Importiamo la libreria turtle
import turtle;

# Apriamo la finestra di gioco
window = turtle.Screen()

# Impostiamo il colore della finestra di gioco:
backgroundColor = window.bgcolor("black")

# Istanziamo due tartarughe che disegneranno i quadrati:
turtleOne = turtle.Turtle()
turtleTwo = turtle.Turtle()

# Diamo velocità lenta alle tartarughe:
turtleOne.speed(1)
turtleTwo.speed(1)

# Istanziamo altre due tartarughe che disegneranno i triangoli
turtleThree = turtle.Turtle()
turtleFour = turtle.Turtle()

# Assegnamo colori di default alle tartarughe:
turtleOneColor = turtleOne.color("blue")
turtleTwoColor = turtleTwo.color("red")
turtleThreeColor = turtleThree.color("green")
turtleFourColor = turtleFour.color("orange")

# Facciamo disegnare 2 quadrati con for loop:
for _ in range(4):
    turtleOne.forward(100)
    turtleOne.left(90)

# Spostiamo la seconda tartaruga 
turtleTwo.sety(-100)

# Facciamo disegnare alla seconda tartaruga il quadrato
for _ in range(4):
    turtleTwo.forward(100)
    turtleTwo.left(90)
    
# Facciamo disegnare 2 triangoli con for loop:

turtleThree.setx(100)

for _ in range(3):
    turtleThree.forward(100)
    turtleThree.left(120)

turtleFour.setx(-100)

for _ in range(3):
    turtleFour.forward(100)
    turtleFour.left(120)


# Manteniamo aperta la finestra di gioco:
window.mainloop()