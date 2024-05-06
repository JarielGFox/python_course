# Boolean expressions

# True or False
# True and False
# True and True
# True or True
# not True
# not False\
    
5 == 5 # valuto se due numeri sono uguali
5 == 7 # valuto se due numeri sono uguali

x == y # .. True se x uguale a y
x != y # .. True se x diverso da y
x > y # .. True se x è maggiore di y
x < y # .. True se x è minore di y
x >= y # .. True se x è maggiore OPPURE uguale a y
x <= y # .. True se x è minore OPPURE ugnuale a y

# Operatori logici or e and

3 < 5 or 4 > 6; # Ritorna true se almeno una è vera
3 < 5 and 4 > 6; # Ritorna false se tutte sono false e ritorna true se entrambe sono vere
not (3 < 5 or 4 > 6); # Ritorna false se almeno una è vera

# Condizioni

if 3 < 5:
    print('3 maggiore di cinque')
elif 3 > 5:
    print('3 maggiore di cinque')
else:
    print('3 = 5')
    