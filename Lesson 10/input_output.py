# usare la funzione open() per aprire un file in modalità di lettura o scrittura
# Apertura e scrittura dei files 

divina = '''Nel mezzo del cammin di nostra vita
mi ritrovai per una selva oscura,
ché la diritta via era smarrita.
Ahi quanto a dir qual era è cosa dura,
esta selva selvaggia e aspra e forte,
che nel pensier rinova la paura!'''

file_divina = open('divina.txt', 'w') # 'w' per scrivere o 'r' per leggere
mio_file = open('sample.txt', 'r') # 'w' per scrivere o 'r' per leggere

print(mio_file.read()) # in questo modo andiamo a leggere il contenuto del file

print(mio_file.readline()) # in questo modo andiamo a leggere una riga del file

for riga in divina.split('\n'): # in questo modo andiamo a leggere tutte le righe del file con un ciclo for
    file_divina.write(f'{riga}\n')

mio_file.close()
file_divina.close()

# Lettura dei files, si legge con il metodo read() 

mio_file = open('sample.txt', 'r', encoding='utf-8') # diamo l'encoding per poter leggere anche i caratteri speciali
print(type(mio_file)) # vediamo il tipo di mio_file
mio_file.close() # chiudiamo il mio_file

file_divina = open('divina.txt', 'r', encoding='utf-8') # diamo l'encoding per poter leggere anche i caratteri speciali
while True: # in questo modo andiamo a leggere il contenuto del file
    verso = file_divina.readline() # in questo modo andiamo a leggere una riga del file
    if len (verso) == 0:
        break
    print(verso)
file_divina.close()


