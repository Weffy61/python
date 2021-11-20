numbers = input('Введите числа => ')
i = 0
for sym in numbers:
    if sym.isdigit():
        i += int(sym)

total = str(i)
with open('hw_5(ls_5).txt', 'w', encoding="utf-8") as f:
    f.writelines(f'Сумма введеных чисел => {total}')

