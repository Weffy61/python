def my_sum ():
    sum_res = 0
    ex = False
    while not ex:
        number = input('Введите цифры через пробил или "*" для выхода - ').split(' ')

        res = 0
        for i in range(len(number)):
            if number[i] == '*':
                ex = True
                break
            else:
                res = res + int(number[i])
        sum_res = sum_res + res
        print('Текущая сумма', sum_res)
    print('Конечная сумма', sum_res)


my_sum()
