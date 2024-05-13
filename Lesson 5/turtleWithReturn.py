'''Aggiungete al turtle program una funzione draw_poly per disegnare qualunque
poligono regolare dati il numero di lati e il numero di passi'''

import turtle

window = turtle.Screen()
turty = turtle.Turtle()

def drawPoly(lati, tartaruga): 
    for _ in range(lati):
        tartaruga.forward(100)
        tartaruga.left(360/lati)
    
drawPoly(int(input('Inserisci il numero di lati: ')), turty)    
    
# Teniamo la finestra del programma aperta
window.mainloop()