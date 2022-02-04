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

##aprire un file di testo leggendo linea per linea
with open('pi_digits.txt') as file_object_line:
    i = 1
    for line in file_object_line:
        print(f'linea {i}) {line.rstrip()}')  # rimuovi il vai a capo
        i += 1

##Making a List of Lines from a File
filename = 'pi_digits.txt'

with open(filename) as file_object_line2:
    linee = file_object_line2.readlines()

for linea in linee:
    print(linea.rstrip())

##Working with a File’s Contents
pi_string = ''
for linea in linee:
    pi_string += linea.strip()

print(pi_string)
print(len(pi_string))

##Large Files: One Million Digits
print(f"{pi_string[:4]}....")   ##[:numero digit] visualizza solo i primi 4 caratteri
# print(len(pi_string))
