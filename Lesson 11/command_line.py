import sys


# Passiamo due numeri come argomenti nel terminale che saranno i parametri della funzione sum. Successivamente chiamiamo la funzione in una variabile e stampiamo il risultato che restituisce i due parametri castati in interi

def sum(a, b):
    return a + b

risultato =  sum(int(sys.argv[1]), int(sys.argv[2]))

print(risultato)