# Leggete il file divina_commedia_extended.txt e scrivete un programma per contare:
# 1. il numero di righe nel file
# il numero di parole nel file
# il numero di caratteri diversi nel file

mio_file = open('divina_commedia_extended.txt', 'r', encoding='utf-8')
print(len(mio_file.readlines()))

mio_file.close()

mio_file = open('divina_commedia_extended.txt', 'r', encoding='utf-8')
parole_splittate = mio_file.read().split(' ')
print(len(parole_splittate))

mio_file.close()

mio_file = open('divina_commedia_extended.txt', 'r', encoding='utf-8')
dizionario = {}

for char in mio_file.read():
    if char.isalpha():
        dizionario[char] = dizionario.get(char, 0) + 1
        
print(dizionario)
    


