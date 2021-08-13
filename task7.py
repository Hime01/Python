def my_factorial(number):
    fact = 1
    for i in range(number + 1):
        yield f'{i}! = {fact}'
        fact = fact * (i + 1)


user_numb = int(input('Введите число, буду показывать факториалы чисел до него включительно: '))
for el in my_factorial(user_numb):
    print(el)
