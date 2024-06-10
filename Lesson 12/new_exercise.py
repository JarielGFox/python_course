'''Creiamo classe studente e chiediamo come parametro nome, cognome, età, classe
Impostiamo un metodo che verifica lo studente sia maggiorenne'''

class Student:
    
    def __init__(self, name: str, surname: str, age: int, course: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.course = course
        
    def is_adult(self):
        if self.age >= 18:
            return (f'Lo studente {self.name} {self.surname} è maggiorenne')
        else:
            return (f'Lo studente {self.name} {self.surname} è minorenne')
        
    def greetings(self):
        print(f'Ciao mi chiamo {self.name} {self.surname} ed ho {self.age} anni! Frequento la classe del corso di {self.course}')
            
            
studente1 = Student('Giovanni', 'Crudele', 35, 'Informatica')
studente1.greetings()
studente1.is_adult()

studente2 = Student('Carlo', 'Coltelli', 27, 'Elettronica')
studente2.greetings()
studente2.is_adult()

studente3 = Student('Marco', 'Zappatore', 29, 'Omicidi')
studente3.greetings()
studente3.is_adult()

studente4 = Student('Gennaro', 'Rampanti', 24, 'Arte')
studente4.greetings()
studente4.is_adult()