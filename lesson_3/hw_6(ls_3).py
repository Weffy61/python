def int_func(string):
    string = string.split(' ')
    words = []
    for i in string:
        title_words = i[0].upper() + i[1:]
        words.append(title_words)
    words = ' '.join(words)
    print(words)


int_func(input('Введите слово или строку =>'))
