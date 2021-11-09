def info(name, lname, bday, city, email, phone):
    return name, lname, bday, city, email, phone


result = info(name=input('[?] Имя => '), lname=input('[?] Фамилия => '), bday=input('[?] День рождения => '),
              city=input('[?] Город => '), email=input('[?] e-mail => '), phone=input('[?] Телефон => '))

print(result)
