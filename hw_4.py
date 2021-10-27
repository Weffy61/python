number = int(input('Enter ur number => '))
result = -1
while number > 10:
    i = number % 10
    number //= 10
    if i > result:
        result = i
print(result)
