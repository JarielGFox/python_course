'''Create un dizionario e passatelo come argomento alla funzione len()'''

mioDizionario = {
    'nome': 'Giovanni',
    'cognome': 'Crudele',
    'eta': 34,
    'citta': 'Nocera'
}

print(len(mioDizionario))

'''Create un oggetto {} e riempitelo con due coppie chiave-valore'''

mioOggetto = {}

mioOggetto['nome'] = 'Giovanni'
mioOggetto['cognome'] = 'Crudele'

# Metodi dei dizionari: keys(), values(), items(), get()

print(mioOggetto.keys())
print(mioOggetto.values())
print(mioOggetto.items())
print(mioOggetto.get('nome'))
