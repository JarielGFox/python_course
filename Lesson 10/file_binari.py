# Lavorare coi binari

soluzione = [3, 6, 2, 7, 1, 4, 0]
bin_file = open('regine.bin', 'wb')
byte_soluzione = bytearray(soluzione)
bin_file.write(byte_soluzione)
bin_file.close()

bin_file = open('regine.bin', 'rb')
contenuto = bin_file.read()
bin_file.close()
print(contenuto)
print(type(contenuto))

