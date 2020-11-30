crypto_letter = []

while True:
    what = input('Введите букву:')
    d = {'a': 'n', 'b': 'o'}
    print(d.get(what, 'буква не найдена'))

    if what == 'stop':
        print(crypto_letter)
        crypto_letter.clear()
        continue

    crypto_letter.append(d.get(what, ''))
    continue
