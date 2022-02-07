def count_words(nomefile: str):
    """

    :type nomefile: str
    """
    try:
        with open(nomefile, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f'Il file {nomefile} non esiste.')
    else:
        # conta il numero di parole nel file
        parole = contents.split()
        num_parole = len(parole)
        print(f'Il file {nomefile} è formato da {num_parole} parole')


nomefile = 'testo.txt'
count_words(nomefile)
