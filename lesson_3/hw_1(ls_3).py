def summ(a, b):
    if b == 0:
        print('Деление на 0')
    else:
        result = a // b
        return result


print(summ(int(input('Введите 1-ое число => ')), int(input('Введите 2-ое число => '))))
