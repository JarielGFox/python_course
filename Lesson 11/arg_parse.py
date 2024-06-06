import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-a', type=int)
parser.add_argument('-b', type=int)
parser.add_argument('-nom1', '-nominativo1', type=str)
parser.add_argument('-nom2', '-nominativo2', type=str)

args = parser.parse_args()

def sum(a, b):
    return a + b

print (sum(args.a, args.b))

def saluta(nominativo1, nominativo2):
    return 'Ciao ' + nominativo1 + ' ' + nominativo2

print(saluta(args.nominativo1, args.nominativo2))