''' Create una lista e vuota e riempitela con un loop for'''
miaLista = []
for i in range(5):
    miaLista.append(i)

print(miaLista)

'''Create una lista con una list comprehension'''

miaLista = []
miaLista = [i for i in range(10)]
print(miaLista)