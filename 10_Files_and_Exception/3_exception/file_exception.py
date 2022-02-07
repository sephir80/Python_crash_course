def count_words(filename: str):
    """

    :type filename: str
    """
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f'Il file {filename} non esiste.')
    else:
        # conta il numero di parole nel file
        parole = contents.split()
        num_parole = len(parole)
        print(f'Il file {filename} è formato da {num_parole} parole')


filenames = ['alice.txt', 'empire.txt', 'migrant.txt']
for filename in filenames:
    count_words(filename)

