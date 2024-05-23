'''Dizionari di Python'''

# I dizionari di Python sono come gli oggetti di JavaScript con la differenza che i dizionari contengono coppie chiave/valore.

mioDizionario = {
    'key1': 'value1', 
    'key2': 'value2'
}

print(mioDizionario['key1'])

# per accedere ai dati in un dizionario usiamo la bracket notation come in JS come se fosse un array. Possiamo avere anche una lista di chiavi e valori, in questo caso il dizionario è un array di coppie chiave/valore.

students = [{
    'name': 'Giovanni',
    'age': 25
}, {
    'name': 'Lorenzo',
    'age': 30
}, {
    'name': 'Marco',
    'age': 35
}, {
    'name': 'Paolo',
    'age': 40
}]


print(students[0]['name'])