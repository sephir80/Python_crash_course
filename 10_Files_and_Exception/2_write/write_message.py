filename = 'programming.txt'

## scrittura di una riga in un file di testo
with open(filename, 'w') as file_object:
    file_object.write("mi piace programmare")

## scrittura di piu righe
with open(filename, 'w') as file_object:
    file_object.write("mi piace programmare")
    file_object.write("vorrei imparare nuovi linguaggi")  ## crea le 2 righe una dopo l'altra

## scrittura di piu righe
with open(filename, 'w') as file_object:
    file_object.write("mi piace programmare.\n")
    file_object.write("vorrei imparare nuovi linguaggi.\n")  ## crea le 2 righe una dopo l'altra

## scrittura di un file in modalità append
with open(filename, 'a') as file_object:
    file_object.write("trovo interesse anche nei dataset\n")
    file_object.write("mi piacciono anche le app che funzionano nei browser\n")
