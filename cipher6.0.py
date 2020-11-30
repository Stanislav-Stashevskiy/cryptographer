crypto_letter = []
what = input('введите имя файла(без .txt):')

file = open(what)
while True:
    d = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'k': 'x', 'l': 'y',
         'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j',
         'x': 'k', 'y': 'l', 'z': 'm', '\n': '\n'}

    for c in file.read():
        crypto_letter.append(d.get(c, 'буква не обнаружена'))
    print(crypto_letter)
    break

what_name = input('Введите название нового файла:')

new_file = open(what_name, 'w')
for index in crypto_letter:
    new_file.write(index)
new_file.close()

crypto_letter.clear()
