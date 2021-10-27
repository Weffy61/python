number = int(input('Введите целое натуральное число => '))
num = [8, 6, 5, 3, 2, 1]
for i in num:
    pos = num.index(i)
    if number >= i:
        num.insert(pos, number)
        break
print(num)


