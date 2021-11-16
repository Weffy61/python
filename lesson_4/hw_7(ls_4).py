def fact(num):
    current = 1
    for i in range(1, num + 1):
        current *= i
        yield current


n = int(input('Введите число => '))
for el in fact(n):
    print(el)
