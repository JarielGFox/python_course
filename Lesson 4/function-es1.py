# Scrivi una funzione che dato un numero in input scriva a monitor il suo quadrato e dica se è pari o dispari

# Dichiariamo la funzione ed assegnamo un parametro a cui daremo il valore integer
def square(number = int):
    print(number ** 2)
    # Se il numero è pari (modulo 2 == 0) stampiamo Pari
    if number % 2 == 0:
        print('Pari')
    # Altrimenti, se la condizione di sopra non è veritiera, stampiamo dispari
    else:
        print('Dispari')

square(int(input('Inserisci un numero: ')))