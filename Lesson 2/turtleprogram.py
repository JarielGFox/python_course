import turtle

# dichiariamo i colori della tartaruga e della sfondo selezionati dall'utente
squirtleColor = input('Colore di Squirtle: ')
turtonatorColor = input('Colore di Turtonator: ')
bgColor = input('Colore sfondo: ')

# crea la finestra di gioco 
window = turtle.Screen() 

# crea la tartaruga, istanziando la classe turtle
squirtle = turtle.Turtle() 
turtonator = turtle.Turtle()

# cambia il colore della tartaruga in base alla scelta dell'utente
squirtle.color(squirtleColor)
turtonator.color(turtonatorColor)
# cambia il colore della sfondo
window.bgcolor(bgColor) 

lati = 4

for i in range(lati):
    squirtle.forward(200)
    squirtle.left(360/lati)
    
    if i > 2:
        squirtle.color("orange")
    

squirtle.write("Hello World!", True, align="left", font=("Arial", 16, "normal"))

for _ in range():
    turtonator.back(100)
    turtonator.right(90)
    
        
turtonator.write("Puppami la fava", True, align="right", font=("Arial", 16, "normal"))

# Ora dobbiamo avere il mainloop attivo e la finestra rimarrà sempre attiva
# loop infinito finche la finestra non viene chiusa
window.mainloop() 


