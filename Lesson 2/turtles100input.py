'''Scrivere un programma come il punto 1. ma i numeri vengono chiesti 10 volte
all'utente con input()'''

testo = 'turtles'

for i in range(10):
    numberTimes = input('Quante volte vuoi che stampo? ')
    print(testo*int(numberTimes))