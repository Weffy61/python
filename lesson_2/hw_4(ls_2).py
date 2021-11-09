# Вы сказали использовать enumerate
lst = input('Введите строку => ')
lst = list(lst.split(' '))
for i in enumerate(lst):
    print(f'{i[:10]}')
print(lst)

# Я сделал и чуток по другому
lst = input('Введите строку => ')
lst = list(lst.split(' '))
for i in lst:
    print(f'{lst.index(i)}. {i[:10]}')
print(lst)
