# Делал данное д/з по вашему разбору, сам пытался через цикл с enumerate, но не удалось

total = {}

with open('hw_6(ls_5).txt', 'r', encoding="utf-8") as f:
    my_list = f.readlines()
    for i in my_list:
        line = i.split()
        hours = 0
        for x in line[1:]:
            if x != '-':
                num = '0'
                for z in x:
                    if z.isdigit():
                        num += z
                    else:
                        break
                hours += int(num)
        total.update({line[0].strip(':'): hours})
print(total)
