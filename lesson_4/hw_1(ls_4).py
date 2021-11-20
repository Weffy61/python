from sys import argv

print(argv)
if len(argv) < 4:
    print('Введите все данные')
else:
    salary = float(argv[1]) * float(argv[2]) + float(argv[3])
    print(salary)

