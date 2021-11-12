t = int(input('Enter time in seconds => '))

hours = t // 3600
minutes = (t % 3600) // 60
sec = (t % 3600) % 60

total = f'{hours:02}:{minutes:02}:{sec:02}'

print('чч:мм:сс')
print(total)


