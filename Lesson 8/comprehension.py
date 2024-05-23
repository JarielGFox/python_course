'''List comprehension, set comprehension e dict comprehension'''

# List comprehension
lista_compr = [i for i in range(10)]
print(lista_compr)

# Set comprehension
set_numeri = {i for i in range(10)}
print(set_numeri)

# Dict comprehension
dict_numeri = {i:i**2 for i in range(10)}
print(dict_numeri)