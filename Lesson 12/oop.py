# Impariamo la programmazione ad oggetti in python 

class Student:
    '''Insieme di informazioni riguardanti uno studente'''
    
    # Il @classmethod è un decoratore, il metodo racchiuso nel decoratore, prende tutta la classe
    @classmethod
    def info(cls):
        print('Informazioni riguardanti uno studente')
    
    # __init__ è il costruttore
    def __init__(self, name: str, age: str):
        self.name = name
        self.age = age
    
    # Greet è il metodo      
    def greet(self):
        print(f'Ciao mi chiamo {self.name} ed ho {self.age} anni.')
        
# Istanziamo una copia della classe Student, passando come argomenti il nome e l'eta' (che ricordiamo devono essere stringhe)
studente = Student('Giovanni', 35)
# Chiamiamo il metodo greet() che ha come argomento la variabile studente
studente.greet()
studente.info()