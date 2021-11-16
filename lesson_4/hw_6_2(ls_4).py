from itertools import cycle


def iterator(phrase, stop):
    x = 0
    for i in cycle(phrase):
        if x > stop:
            break
        print(i)
        x += 1


phrase = input('Введите строку для итерации => ')
stop = int(input('Введите колличество повторений => '))

print(iterator(phrase=phrase, stop=stop))
