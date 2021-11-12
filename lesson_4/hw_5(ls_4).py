from functools import reduce


def mult(prev, curr):
    return prev * curr


my_list = [i for i in range(100, 1001) if i % 2 == 0]
total = reduce(mult, my_list)
print(total)






