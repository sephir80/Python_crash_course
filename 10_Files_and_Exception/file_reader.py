
### versione con dichiarazione <<with>>. with chiude in automatico il file una volta completato il ciclo interno
###       oppure all'occorenza di un errore

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)


## metodo classico per gestione dei file
file_object2 = open('pi_digits.txt')
contenuto = file_object2.read()
print(contenuto)
file_object2.close()

## aprire un file di testo in una sottocartella con percorso relativo
with open('text_files/testo_caso.txt') as file_object3:
    contents = file_object3.read()
print(contents)
