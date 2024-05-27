# Formattazione delle stringhe in Python

nome = 'Giangeppo'
anni = 42
altezza = 1.75  

# formattazione classica con concatenazione di stringhe + variabili
output = 'Il mio nome è ' + nome + ' ho ' + str(anni) + ' anni, ' + ' sono alto ' + str(altezza) + ' metri.'
print(output)

# formattazione delle stringhe in Python new style
output2 = 'Il mio nome è {0} ho {1} anni, sono alto {2} metri.'.format(nome, anni, altezza)
print(output2)

# formattazione fstrings, si mette la "f" prima della stringa e poi tipo template literal di JS le variabili tra parentesi graffe   
output3 = f'Il mio nome è {nome} ho {anni} anni, sono alto {altezza} metri.'
print(output3)