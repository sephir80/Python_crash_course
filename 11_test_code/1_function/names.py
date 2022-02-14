from name_function import get_formatted_name

print("inserisci 'q' per terminare in qualsiasi momento")
while True:
    first = input("\nInserisci il nome: ")
    if first == 'q':
        break
    last = input("\nInserisci il cognome: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNome in formato ordinato: {formatted_name}.")
