''' Create una lista e vuota e riempitela con un loop for'''
miaLista = []
for i in range(5):
    miaLista.append(i)

print(miaLista)

'''Create una lista con una list comprehension'''
miaLista = [i for i in range(10)]
print(miaLista)

'''Usando una dict comprehension, create un dizionario per mappare la stringa "x" al quadrato di x dove x è un numero che va da 2 a 22'''

mioDict = {str(i**2): i**2 for i in range(23)}
print(mioDict)