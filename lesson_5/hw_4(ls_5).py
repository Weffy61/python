translator = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
total = []
with open('hw_4(ls_5).txt', 'r', encoding="utf-8") as f:
    my_list = f.readlines()
    for i in my_list:
        num = i.split()
        if num[0] in translator:
            total.append(translator[num[0]] + ' — ' + num[2] + '\n')
with open('hw_4(ls_5).txt', 'w', encoding="utf-8") as f:
    f.writelines(total)
    print(total)
