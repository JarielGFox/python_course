'''Modificare il codice al punto 2. per scrivere solo i numeri pari multipli di 3 e i numeri
dispari multipli di 5'''

numberRangeStart = input('Inserisci un range di numeri iniziale: ')
numberRangeEnd = input('Inserisci un range di numeri finale: ')

for i in range(int(numberRangeStart), int(numberRangeEnd)):
    if i % 3 == 0 and i % 5 == 0:
       print('Pari multiplo di 3 e dispari multiplo di 5: ', i)
    elif i % 3 == 0:
        print('Pari multiplo di 3: ', i)
    elif i % 5 == 0:
        print('Dispari multiplo di 5: ', i)