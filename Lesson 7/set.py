# Un set è una lista di valori che non possono essere ripetuti, non è ordinato e non è modificabile (salvo alcune operazioni con i metodi).

mioSet = {1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3}

# possiamo modificare i set con alcuni metodi built in: update(), discard(), remove(), update(), clear()
# add() aggiunge un solo elemento al set
# update() aggiunge un set di elementi al set
# remove() rimuove un elemento dal set, restituisce un errore se l'elemento non è presente
# discard() rimuove un elemento dal set (non viene notificato l'elemento che si sta rimuovendo, ma il set rimane inalterato)

set_numeri = {7, 11, 9}
print(set_numeri)
set_numeri.add(17)
print(set_numeri)
