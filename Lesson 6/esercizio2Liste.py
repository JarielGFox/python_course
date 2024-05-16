'''Create una lista e provate ad utilizzare i metodi: insert(), count(), remove(), extend(), index(), sort(), remove()'''

listaNuova = ['Pizza', 'Insalata', 'Cheeseburger', 'Carne', 'Pollo']
listaNuova.remove('Carne')
listaNuova.extend(['Ciao', 'a', 'tutti', '!'])
listaNuova.insert(0, 'Ciao')
print(listaNuova.index('Ciao'))
print(listaNuova.count('Pollo'))
print(listaNuova)