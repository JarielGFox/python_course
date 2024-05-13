# Funzioni ricorsive:

# Una funzione che richiama se stessa

def fibonacci(n):
    if n <= 1:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(6))
    