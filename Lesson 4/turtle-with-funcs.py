import turtle

# Avvio la finestra di lancio
window = turtle.Screen()

# Impostiamo il colore nero di bg
window.bgcolor("black")

# Istanziamo una tartaruga
squirtle = turtle.Turtle()

# Dichiariamo una funzione che determini che figura geometrica disegnare:
def pictureToDraw():
    # Chiediamo all'utente la lunghezza lato del poligono
    userQuestion = input("Inserisci la lunghezza lato del poligono: ")
    
    # Tutto il codice che abbiamo usato per determinare condizione e cicli, lo inseriamo nella funzione pictureToDraw
    if int(userQuestion) % 2 == 0:
        for _ in range(4):
            squirtle.forward(100)
            squirtle.left(90)
        squirtle.penup()
        squirtle.setx(-200)
        squirtle.pendown()
        squirtle.write('Ecco a te un quadrato!', True, align="left", font=("Arial", 16, "normal")) 
    else:
        for _ in range(3):
            squirtle.forward(100)
            squirtle.left(120)
        squirtle.penup()
        squirtle.setx(-200)
        squirtle.pendown()
        squirtle.write('Ecco a te un triangolo!', True, align="left", font=("Arial", 16, "normal"))

# Creiamo una funzione che chieda all'utente che colore vogliamo assegnare alla nostra tartaruga squirtle
def chooseColor(colore = str):
    squirtle.color(colore)

# Settiamo la velocità della tartaruga ad 1
squirtle.speed(1)

# Chiediamo all'utente di che colore vuole la sua tartaruga:
chooseColor(input('Inserisci il tuo colore: '))

# Mostriamo un messaggio nel programma per informare l'utente di controllare il terminale
squirtle.write('Controlla il terminale!', True, align="left", font=("Arial", 16, "normal"))
turtle.ontimer(squirtle.clear, 2500)

# Invochiamo la funzione di disegno
pictureToDraw()

# Manteniamo aperta la finestra di gioco
window.mainloop()