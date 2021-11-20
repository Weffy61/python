with open('hw_2(ls_5).txt', 'r') as f:
    my_lines = f.readlines()

lines = 0
words = 0


for line in my_lines:
    lines += 1

    for word in line:
        words = len(line.split())
    print(f'В строке => {lines}, колличество слов => {words}')


print(f'Всего строк => {lines}')
