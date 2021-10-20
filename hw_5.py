revenue = int(input('Enter ur revenue => '))
cost = int(input('Enter ur costs => '))
total = revenue - cost

if cost > revenue:
    print('Вы работаете в убыток =>', total)
elif cost == revenue:
    print('Вы работаете в 0')
else:
    print('Ваш заработок составляет =>', total)
    workers = int(input('Введите колличество сотрудников => '))
    payment = total / workers
    print('Заработная плата на одного сотрудника =>', payment)

