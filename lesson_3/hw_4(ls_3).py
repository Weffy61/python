def my_funk(x, y):
    if x < 0:
        return 'X должен быть больше 0'
    if y > 0:
        return 'Y должен быть меньше 0'
    y = -y
    z = x
    for i in range(1, y):
        x *= z
    result = 1 / x
    return result


total = my_funk(float(input('Введите число возводимое в степень => ')), int(input('Введите отрицательную степень => ')))
print(total)





# print(my_funk(10, -3))









# def my_funk(x, y):
#     z = y
#     while z == 0:
#         y *= 2
#         z += 1
#     total = x * y
#     return total
#
#
# calc = my_funk(10, -3)
# print(calc)