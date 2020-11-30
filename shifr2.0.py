def main():
    what = input('Введите букву:')
    d = {'a': 'n', 'b': 'o'}
    print(d.get(what, 'буква не найдена'))

    if what == 'stop':
        print(crypto_letter)
        crypto_letter.clear()
        main()

    crypto_letter.append(d.get(what, ''))
    main()


if __name__ == '__main__':
    crypto_letter = []
    main()
