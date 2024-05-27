# Prendiamo il testo seguente e lavoriamoci un po' su.

cantoCommedia = '''Nel mezzo del cammin di nostra vita
mi ritrovai per una selva oscura,
ché la diritta via era smarrita.
Ahi quanto a dir qual era è cosa dura,
esta selva selvaggia e aspra e forte,
che nel pensier rinova la paura!'''

versoReverso = "ché la diritta via era smarrita."

# Contate le righe (di effettivo testo) che compongono l'estratto
print(len(cantoCommedia.splitlines()))

# Contiamo le parole nel testo
cantoContato = len(cantoCommedia.split())
print(cantoContato)

# Scrivete al contrario il terzo verso
print(versoReverso.split()[::-1])

# Create un dizionario che mappi ogni carattere (chiave) con la sua occorrenza nel testo (valore)
def occorrenze(testo):
    dizionarioCanto  = {}
    specialChars = [' ', '!', ',', '.']
    for lettera in testo:
        lettera = lettera.casefold()
        if lettera not in specialChars:
                continue
        if lettera in dizionarioCanto:
            dizionarioCanto[lettera] += 1
        else:
            dizionarioCanto[lettera] = 1

    return dizionarioCanto

print(occorrenze(cantoCommedia))

print('selva' in cantoCommedia)

def find_index(testo, parola):
    return testo.index(parola)

print(find_index(cantoCommedia, 'selva'))