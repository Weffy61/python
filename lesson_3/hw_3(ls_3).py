def my_func(a, b, c):
    if a >= b >= c:
        return a + b
    elif a >= c >= b:
        return a + c
    elif b >= a >= c:
        return b + a
    elif b >= c >= a:
        return b + c
    elif c >= a >= b:
        return c + a
    elif c >= b >= a:
        return c + b


print(my_func(int(input('Введите 1 число => ')), int(input('Введите 2 число => ')), int(input('Введите 3 число => '))))
