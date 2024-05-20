'''Create una lista e provate a passare un float all'operatore di indicizzazione []'''

miaLista = ["Pizza" , "Insalata" , "Cheeseburger" , "Carne" , "Pollo"]
miaLista.append(float(15.9))

print(miaLista)

miaListaDue = ["Pizza" , "Insalata" , "Cheeseburger" , "Carne" , "Pollo"]
miaListaDue[2] = float(15.9)
print(miaListaDue)