def print_user(name, surname, year, city, email, numb):
    print(
        f'Имя: {name}\nФамилия: {surname}\nГод рождения: {year}\nГород проживания: {city}\nПочта: {email}\nНомер телефона: {numb}')


print_user(name=input('Введите свое имя: '), surname=input('Введите свою фамилию: '),
           year=input('Введите свой год рождения: '), city=input('Введите свой город проживания: '),
           email=input('Введите свою почту: '), numb=input('Введите свой номер телефона: '))
