# Prendiamo la seguente rubrica (costruita con dizionari annidati):

rubrica = {
    'Paolino Paperino': 
    {
        'giorno': 9,
        'mese': 'agosto',
        'anno': 1934,
        'età': 87,
        'sesso': 'M',
        'mail': 'paolino.paperin0@disney.org'
    },
    
    'Ron Weasley': 
        {
        'giorno': 1, 
        'mese': 'maggio', 
        'anno': 1980, 
        'età': 41, 
        'sesso': 'M',
        'mail': 'ron_weasley80@hogwards.uk'
        },
        
    'Ramona Flowers': 
        {
            'giorno': 18, 
            'mese': 'ottobre', 
            'anno': 2004, 
            'età': 42, 
            'sesso': 'F', 'mail': 'ramona.fls@gmail.com'
        },
        
    'Madoka Ayukawa': 
        {
        'giorno': 25, 
        'mese': 'luglio', 
        'anno': 1969, 
        'età': 52, 
        'sesso':'F', 
        'mail': 
        'madoka_sax@asahi_net.jp'
    }
}


 
for nome, dati in rubrica.items():
        
        if dati["sesso"] == 'M':
            suffix = "o"
        else:
            suffix = "a"
    
message = f"Car{suffix} {nome}, sei nat{suffix} il {dati['giorno']} di {dati['mese']} del {dati['anno']} e quindi a breve compirai {dati['età']+1} anni. Ti manderemo gli auguri a {dati['mail']}"

print(message)

'''A partire dalla rubrica, costruire la lista delle età, ordinata in ordine crescente'''

listaEta = []

for chiave, valore in rubrica.items():
    eta = valore['età']
    listaEta.append(eta)

listaEta.sort()

print(listaEta[::-1])

'''Riorganizzare la rubrica in ordine crescente di età dei personaggi'''

newDictionary = {}
lista_nuova = list(rubrica.items())

def ordine_eta(item):
    return item[1]['età']

#callback in python si fa con key=ordine_eta
lista_nuova.sort(key=ordine_eta)
    
lista_nuova = {nome: value for nome, value in lista_nuova}
    
print(lista_nuova)

