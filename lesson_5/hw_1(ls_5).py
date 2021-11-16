list_0 = []
while True:
    list_1 = input('Введите строку => ')
    if not list_1:
        break
    else:
        list_2 = list_1 + '\n'
        list_0.append(list_2)

with open('hw_1.txt', 'a') as f:
    f.writelines(list_0)
