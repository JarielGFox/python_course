'''Leggete il file rubrica.txt, stampatene il contenuto e create un dizionario che abbia come chiavi i nomi delle colonne e come valori associati la lista dei valori della
colonna'''

# Apriamo il file
file_rubrica = open('rubrica.txt', 'r', encoding='utf-8')

# Leggiamo tutte le righe del file
nominativi = file_rubrica.readlines()

# Chiudiamo il file o ci rompe le scatole 
file_rubrica.close()

# Creiamo dizionario vuoto dando già lo scheletro di base
dizionario_rubrica = {'Nome': [], 'Cognome': [], 'Telefono': []}

# Cicliamo le righe del file
for nominativo in nominativi:
    # Strippiamo gli spazi ai lati
    nominativo = nominativo.strip()
    
    # Se nominativo è vuoto (false), passa alla prossima riga
    if not nominativo:
        continue
    
    # Dividiamo la riga che contiene i nominativi nel formato chiave, valore come nei dizionari
    chiave, valore = nominativo.split(':')
    
    # Creiamo la casistica per aggiungere il valore alla lista corrispondente nel dizionario:
    if chiave == 'Nome':
        dizionario_rubrica['Nome'].append(valore)
    elif chiave == 'Cognome':
        dizionario_rubrica['Cognome'].append(valore)
    elif chiave == 'Telefono':
        dizionario_rubrica['Telefono'].append(valore)

print(dizionario_rubrica)