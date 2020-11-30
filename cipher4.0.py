crypto_letter = []

while True:
    d = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a','o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm', ' ': ' '}
    what = input('Введите слово:')
    for c in what:
        crypto_letter.append(d.get(c, 'буква не обнаружена'))
    print(crypto_letter)
    crypto_letter.clear()
