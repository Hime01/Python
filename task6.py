from itertools import count, cycle

my_list = ['first', 'second', 'third']
cycled = 0
for el in cycle(my_list):
    if cycled > 10:
        break
    cycled += 1
    print(el)

start_count = input('Введите целое число, с которого будем генерировать числа: ')

try:
    start_count = int(start_count)
    counts = 0
    for numb in count(start_count):
        if counts > 10:
            break
        counts += 1
        print(numb)
except ValueError:
    print(f'{start_count} - не целое число. Скрипт прерван.')