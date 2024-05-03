"""Utilizzando la funzione input() , chiedete all'utente:
tra quante ore mettere la sveglia
e visualizza su schermo l'ora che segnerà l'orologio quando suonerà la sveglia"""
import datetime

AlarmTime = input('Tra quante ore mettere la sveglia? ')
now = input('Ora attuale? ')
TimeToWakeUp = float(AlarmTime) + float(now)
print('La sveglia suonerà alle ore: ' + str(TimeToWakeUp))
