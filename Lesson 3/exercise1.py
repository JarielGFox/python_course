# Booleans and if statements

'''Scrivere un codice che chieda in input all'utente un range di numeri (inizio e fine) e
poi stampi a video solo i numeri pari'''

numberRangeStart = input('Inserisci un range di numeri iniziale: ')
numberRangeEnd = input('Inserisci un range di numeri finale: ')

for i in range(int(numberRangeStart), int(numberRangeEnd)):
    if i % 2 == 0: 
        print(i)