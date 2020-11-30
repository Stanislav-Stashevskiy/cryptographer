what = input('Зашифровать или расшифровать?(1 или 2):')


def vvod():
    a1 = ' '
    a2 = ' '
    a3 = ' '
    a4 = ' '
    a5 = ' '
    a6 = ' '
    a7 = ' '
    a8 = ' '
    a9 = ' '
    a10 = ' '
    a11 = ' '
    a12 = ' '
    a13 = ' '
    a14 = ' '
    a15 = ' '
    a16 = ' '
    a17 = ' '
    a18 = ' '
    a19 = ' '
    a20 = ' '
    a21 = ' '
    a22 = ' '
    a23 = ' '
    a24 = ' '
    a25 = ' '
    for i in range(10):
        a = input('Введите букву:')
        if a == 'a':
            a1 = 'b'
        elif a == 'b':
            a2 = 'a'
        elif a == 'c':
            a3 = 'd'
        elif a == 'd':
            a4 = 'c'
        elif a == 'e':
            a5 = 'f'
        elif a == 'f':
            a6 = 'e'
        elif a == 'g':
            a7 = 'h'
        elif a == 'h':
            a8 = 'g'
        elif a == 'i':
            a9 = 'j'
        elif a == 'j':
            a10 = 'i'
        elif a == 'k':
            a11 = 'l'
        elif a == 'l':
            a12 = 'k'
        elif a == 'm':
            a13 = 'n'
        elif a == 'n':
            a13 = 'm'
        elif a == 'o':
            a14 = 'p'
        elif a == 'p':
            a15 = 'o'
        elif a == 'q':
            a16 = 'r'
        elif a == 'r':
            a17 = 'q'
        elif a == 's':
            a18 = 't'
        elif a == 't':
            a19 = 's'
        elif a == 'u':
            a20 = 'v'
        elif a == 'v':
            a21 = 'u'
        elif a == 'w':
            a22 = 'x'
        elif a == 'x':
            a23 = 'w'
        elif a == 'y':
            a24 = 'z'
        elif a == 'z':
            a25 = 'y'
        elif a == 'stop':
            print(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25)


if what == '1':
    vvod()