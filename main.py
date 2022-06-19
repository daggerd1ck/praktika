import math

print('Привет! Эта программа шифрует и расшифровывает сообщения d=====(^_^ *)b\nЧто вы хотите сделать?\n1. Шифрование;\n2. Расшифрование.\n\nUPD: символы "*" при выводе зашифрованного сообщения являются незначимыми, требуются для расшифровки.') #очень френдли же?
shifr = int(input())
if shifr == 1:
    print('\nВведите вид элемента перестановки:\n1. Символ;\n2. Несколько символов;\n3. Слово.')
    element = int(input())
    if element == 1:
        print('\nВведите ключ шифрования (позиции вводятся через пробел, например, "1 0 3 2"):')
        klyuch = input()
        klyuch = list(map(int, klyuch.split()))
        print('\nВведите сообщение, которое хотите зашифровать:')
        soobshenie = input()
        dlinaklyucha = len(klyuch)
        dlinasoobshenie = len(soobshenie)
        zashifr = ''
        kolvodlin = dlinasoobshenie / dlinaklyucha
        kratnost = math.ceil(kolvodlin)
        ostatok = dlinasoobshenie % dlinaklyucha
        if ostatok != 0:
            soobshenie += (dlinaklyucha - ostatok) * '*'
            dlinasoobshenie = len(soobshenie)
            for i in range(0, kratnost):
                for j in range(0, dlinaklyucha):
                    zapominalka = klyuch[j]
                    zashifr += soobshenie[int(zapominalka)]
                soobshenie = soobshenie[dlinaklyucha:]
            print('\nЗашифрованное сообщение: ', zashifr)

        else:
            for i in range(0, kratnost):
                for j in range(0, dlinaklyucha):
                    zapominalka = klyuch[j]
                    zashifr += soobshenie[int(zapominalka)]
                soobshenie = soobshenie[dlinaklyucha:]
            print('\nЗашифрованное сообщение: ', zashifr)


    if element == 2:
        print('\nВведите количество символов:')
        skoksimvolov = int(input())
        print('\nВведите ключ шифрования (позиции вводятся через пробел, например, "1 0 3 2"):')
        klyuch2 = input()
        klyuch2 = list(map(int, klyuch2.split()))
        print('\nВведите сообщение, которое хотите зашифровать:')
        soobshenie2 = input()
        dlinaklyucha2 = len(klyuch2)
        dlinasoobshenie2 = len(soobshenie2)
        zashifr2 = ''
        kolvoblokov = dlinasoobshenie2 % skoksimvolov
        bloki = dlinasoobshenie2 // skoksimvolov
        if kolvoblokov != 0:
            skokdopisat = skoksimvolov - kolvoblokov
            soobshenie2 += skokdopisat * '*'
            dlinasoobshenie2 = len(soobshenie2)
            kolvoblokov = dlinasoobshenie2 // skoksimvolov
            q = kolvoblokov % dlinaklyucha2
            if q != 0:
                soobshenie2 += (dlinaklyucha2 - q) * skoksimvolov * '*'
                dlinasoobshenie2 = len(soobshenie2)
                kratnost2 = dlinasoobshenie2 // skoksimvolov // dlinaklyucha2
                for i in range(0, kratnost2):
                    for j in range(0, dlinaklyucha2):
                        zapominalka2 = klyuch2[j]
                        for k in range(0, skoksimvolov):
                            index = zapominalka2 * skoksimvolov + k
                            zashifr2 += soobshenie2[index]
                    soobshenie2 = soobshenie2[(dlinaklyucha2 * skoksimvolov):]
                print('\nЗашифрованное сообщение: ', zashifr2)
            else:
                kratnost2 = dlinasoobshenie2 // skoksimvolov // dlinaklyucha2
                for i in range(0, kratnost2):
                    for j in range(0, dlinaklyucha2):
                        zapominalka2 = klyuch2[j]
                        for k in range(0, skoksimvolov):
                            index = zapominalka2 * skoksimvolov + k
                            zashifr2 += soobshenie2[index]
                    soobshenie2 = soobshenie2[(dlinaklyucha2 * skoksimvolov):]
                print('\nЗашифрованное сообщение: ', zashifr2)
        else:
            q = bloki % dlinaklyucha2
            if q != 0:
                soobshenie2 += (dlinaklyucha2 - q) * skoksimvolov * '*'
                dlinasoobshenie2 = len(soobshenie2)
                kratnost2 = dlinasoobshenie2 // skoksimvolov // dlinaklyucha2
                for i in range(0, kratnost2):
                    for j in range(0, dlinaklyucha2):
                        zapominalka2 = klyuch2[j]
                        for k in range(0, skoksimvolov):
                            index = zapominalka2 * skoksimvolov + k
                            zashifr2 += soobshenie2[index]
                    soobshenie2 = soobshenie2[(dlinaklyucha2 * skoksimvolov):]
                print('\nЗашифрованное сообщение: ', zashifr2)
            else:
                kratnost2 = dlinasoobshenie2 // skoksimvolov // dlinaklyucha2
                for i in range(0, kratnost2):
                    for j in range(0, dlinaklyucha2):
                        zapominalka2 = klyuch2[j]
                        for k in range(0, skoksimvolov):
                            index = zapominalka2 * skoksimvolov + k
                            zashifr2 += soobshenie2[index]
                    soobshenie2 = soobshenie2[(dlinaklyucha2 * skoksimvolov):]
                print('\nЗашифрованное сообщение: ', zashifr2)


    if element == 3:
        print('\nВведите ключ шифрования (позиции вводятся через пробел, например, "1 0 3 2"):')
        klyuch3 = input()
        klyuch3 = list(map(int, klyuch3.split()))
        print('\nВведите сообщение, которое хотите зашифровать:')
        soobshenie3 = input()
        soobshenie3 = soobshenie3.split(" ")
        dlinaklyucha3 = len(klyuch3)
        dlinasoobshenie3 = len(soobshenie3)
        zashifr3 = ''
        slovavklyuche = dlinasoobshenie3 / dlinaklyucha3
        ostatok3 = dlinasoobshenie3 % dlinaklyucha3
        if ostatok3 != 0:
            print(soobshenie3)
            soobshenie3.append((dlinaklyucha3 - ostatok3) * '***')
            print(soobshenie3)
            dlinasoobshenie3 = len(soobshenie3)
            kratnost3 = dlinasoobshenie3 // dlinaklyucha3
            for i in range(0, kratnost3):
                for j in range(0, dlinaklyucha3):
                    zapominalka3 = klyuch3[j]
                    zashifr3 += soobshenie3[int(zapominalka3)] + ' '
                soobshenie3 = soobshenie3[dlinaklyucha3:]
            print('\nЗашифрованное сообщение: ', zashifr3)
        else:
            kratnost3 = dlinasoobshenie3 // dlinaklyucha3
            for i in range(0, kratnost3):
                for j in range(0, dlinaklyucha3):
                    zapominalka3 = klyuch3[j]
                    zashifr3 += soobshenie3[int(zapominalka3)] + ' '
                soobshenie3 = soobshenie3[dlinaklyucha3:]
            print('\nЗашифрованное сообщение: ', zashifr3)

            '''РАСШИФРОВКА'''

if shifr == 2:
    print('\nВведите вид элемента расшифровки:\n1. Символ;\n2. Несколько символов;\n3. Слово.')
    element = int(input())
    if element == 1:
        print('\nВведите ключ шифрования (позиции вводятся через пробел, например, "1 0 3 2"):')
        klyuch = input()
        klyuch = list(map(int, klyuch.split()))
        print('\nВведите сообщение, которое хотите расшифровать:')
        soobshenie = input()
        dlinaklyucha = len(klyuch)
        dlinasoobshenie = len(soobshenie)
        zashifr = [''] * dlinasoobshenie
        kolvodlin = dlinasoobshenie // dlinaklyucha
        for i in range(0, kolvodlin):
            for j in range(0, dlinaklyucha):
                zapominalka = klyuch[j] + (i * dlinaklyucha)
                zashifr[int(zapominalka)] += soobshenie[j]
            soobshenie = soobshenie[dlinaklyucha:]
        str_zashifr = ''.join(zashifr)
        gotovzashifr = str_zashifr.replace('*', '')
        print('\nРасшифрованное сообщение: ', gotovzashifr)


    if element == 2:
        print('\nВведите количество символов:')
        skoksimvolov = int(input())
        print('\nВведите ключ шифрования (позиции вводятся через пробел, например, "1 0 3 2"):')
        klyuch2 = input()
        klyuch2 = list(map(int, klyuch2.split()))
        print('\nВведите сообщение, которое хотите расшифровать:')
        soobshenie2 = input()
        dlinaklyucha2 = len(klyuch2)
        dlinasoobshenie2 = len(soobshenie2)
        zashifr2 = [''] * dlinasoobshenie2
        kratnost2 = dlinasoobshenie2 // skoksimvolov // dlinaklyucha2
        for i in range(0, kratnost2):
            for j in range(0, dlinaklyucha2):
                zapominalka2 = klyuch2[j] + (i * dlinaklyucha2)
                for k in range(0, skoksimvolov):
                    index = zapominalka2 * skoksimvolov + k
                    index2 = (j * skoksimvolov) + k
                    zashifr2[int(index)] += soobshenie2[index2]
            soobshenie2 = soobshenie2[(dlinaklyucha2 * skoksimvolov):]
        str_zashifr = ''.join(zashifr2)
        gotovzashifr = str_zashifr.replace('*', '')
        print('\nРасшифрованное сообщение: ', gotovzashifr)

    if element == 3:
        print('\nВведите ключ шифрования (позиции вводятся через пробел, например, "1 0 3 2"):')
        klyuch3 = input()
        klyuch3 = list(map(int, klyuch3.split()))
        print('\nВведите сообщение, которое хотите расшифровать:')
        soobshenie3 = input()
        soobshenie3 = soobshenie3.split(" ")
        dlinaklyucha3 = len(klyuch3)
        dlinasoobshenie3 = len(soobshenie3)
        zashifr3 = [''] * dlinasoobshenie3
        kratnost3 = dlinasoobshenie3 // dlinaklyucha3
        for i in range(0, kratnost3):
            for j in range(0, dlinaklyucha3):
                zapominalka3 = klyuch3[j] + (i * dlinaklyucha3)
                zashifr3[int(zapominalka3)] += soobshenie3[j] + ' '
            soobshenie3 = soobshenie3[dlinaklyucha3:]
        str_zashifr3 = ''.join(zashifr3)
        gotovzashifr3 = str_zashifr3.replace('***', '')
        print('\nРасшифрованное сообщение: ', gotovzashifr3)