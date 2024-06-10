'''Modificare la classe Punto aggiungendo il metodo distanza_da_punto che
calcola la distanza da un secondo punto (Punto)'''
class Punto:
 
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def distanza_da_punto(self, altro):
        return (abs (self.x - altro.x) + abs(self.y - altro.y))**0.5
    
punto1 = Punto(0, 0)
punto2 = Punto(3, 4)
 
print(punto1.distanza_da_punto(punto2))