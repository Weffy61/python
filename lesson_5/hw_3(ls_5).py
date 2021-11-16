# оч. долго мучался, поэтому сделал, как смог)

with open('hw_3(ls_5).txt', 'r', encoding="utf-8") as f:
    my_lines = f.readlines()

workers = 0
total_salary = 0
low_salary = []

for salary in my_lines:
    worker = salary.split()
    workers += 1

    for i in worker:
        if i < '20000':
            low_salary.append(worker[0])
        try:
            total_salary += float(worker[1]) / 2
        except:
            pass

total_salary = round(total_salary, 2)
average_salary = round(total_salary / workers, 2)
low_salary = ', '.join(low_salary)

print(f'З/п менее 20к имеют: {low_salary}, средняя з/п составляет {average_salary}')