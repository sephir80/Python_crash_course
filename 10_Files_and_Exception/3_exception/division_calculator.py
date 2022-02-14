print('Inserisci due numeri è io li dividerò')
print("enter 'q' to quit")

while True:
    first_number = input("\nPrimo Numero: ")
    if first_number == 'q':
        break
    second_number = input('Secondo numero: ')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('non posso dividere per zero!')
    else:
        print(f'{first_number}/{second_number}={answer}')