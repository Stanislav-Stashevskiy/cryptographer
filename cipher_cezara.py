letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
'x' ,'y', 'z', ' ']
crypto_letters = []
s = [' ', '!', '?', '(', ')']

do = input('Зашифровать или разшифровать?(1/2):')
if do == '1':
    cod = input('Введите код RОТ(1, 2, 3, 4...25):')
    cod = int(cod)
    while True:
        what = input('Введите слово:')

        if what == 'stop':
            break

        for c in what:
            if c in s:
                crypto_letters.append(c)
                continue
            ind_c = letters.index(c)
            crypto_index = ind_c + cod
            if crypto_index > 25:
                crypto_index = 25 - ind_c
            letter = letters[crypto_index]
            crypto_letters.append(letter)
        print(crypto_letters)
        crypto_letters.clear()
    print('Программа завершена!!!')

elif do == '2':
    cod = input('Введите код RОТ(1, 2, 3, 4...25):')
    cod = int(cod)
    while True:
        what = input('Введите слово:')

        if what == 'stop':
            break

        for c in what:
            if c in s:
                crypto_letters.append(c)
                continue
            ind_c = letters.index(c)
            crypto_index = ind_c - cod
            if crypto_index > 25:
                crypto_index = 25 + ind_c
            letter = letters[crypto_index]
            crypto_letters.append(letter)
        print(crypto_letters)
        crypto_letters.clear()
    print('Программа завершена!!!')
