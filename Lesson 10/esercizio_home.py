'''Leggete il file rubrica.txt, stampatene il contenuto e create un dizionario che abbia come chiavi i nomi delle colonne e come valori associati la lista dei valori della
colonna'''

# Apriamo il file
file_rubrica = open('rubrica.txt', 'r', encoding='utf-8')

# Leggiamo tutte le righe del file
nominativi = file_rubrica.read().split('\n')

# Chiudiamo il file o ci rompe le scatole 
file_rubrica.close()

# Creiamo dizionario vuoto dando già lo scheletro di base
dizionario_rubrica = {}

# Cicliamo le righe del file
for nominativo in nominativi:
    nominativo = nominativo.removeprefix('\ufeff').split('\n')
    dati = [dato.split(':')[1].strip() for dato in nominativo]
    dizionario_rubrica[dati[0]] = dati[1:]


print(dizionario_rubrica)