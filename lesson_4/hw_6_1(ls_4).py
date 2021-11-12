from itertools import count


def gen_num(start, stop):
    for i in count(start):
        if i > stop:
            break
        else:
            print(i)


start = int(input('Введите начальное число => '))
stop = int(input('Введите конечное число => '))

print(gen_num(start=start, stop=stop))

