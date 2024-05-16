'''Create un programma che disegna 5 quadrati allineati ed equispaziati. la dimensione dei quadrati la fornisce l'utente. Quando hai terminato di disegnare un quadrato, ti sposti a destra o sinistra (dove ti pare) di larghezza quadrato + X, dove X lo definisci tu arbitrariamente, larghezza quadrato te la da l'utente'''

import turtle

window = turtle.Screen()
turty = turtle.Turtle()
window.bgcolor("black")

# Inizializziamo la variabile massimale al di fuori della funzione per far si che abbia global scope
massimale = 0

def drawSquares20Feet(forward, tartaruga): 
    # Richiamiamo la variabile massimale all'interno della funzione
    global massimale
    # Impostiamo il colore rosso
    tartaruga.color('red')
    for _ in range(5):
        # Disegniamo 5 quadrati
        for _ in range (4):
            tartaruga.forward(forward)
            tartaruga.left(90)
        massimale += 1
        tartaruga.penup()
        forward += 20
        tartaruga.pendown()

# drawSquares20Feet(int(input('Inserisci la lunghezza del lato: ')), turty)    
drawSquares20Feet(int(input('Inserisci la lunghezza del lato: ')), turty)

# Teniamo la finestra del programma aperta
window.mainloop()