'''Modificare il codice al punto 1. per scrivere pari: e il numero se quest'ultimo è
pari, altrimenti scrivere dispari: e il numero'''

numberRangeStart = input('Inserisci un range di numeri iniziale: ')
numberRangeEnd = input('Inserisci un range di numeri finale: ')

for i in range(int(numberRangeStart), int(numberRangeEnd)):
    if i % 2 == 0: 
        print('Pari: ', i)
    else:
        print('Dispari: ', i)  