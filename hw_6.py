a = float(input('[?] Сколько км пробежал спортсмен в 1-ый день => '))
b = float(input('[?] Какая цель в км => '))
days = 1
res = a
while res <= b:
    res += (a * 0.1)
    days += 1
    print(days, '-ый день:', round(res, 2))

print('Цель достигнута на ', days, 'день')
