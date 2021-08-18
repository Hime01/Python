from random import randint

random_list = [randint(1, 1000) for i in range(20)]
print(random_list)
print(f'Сумма случайных чисел: {sum(random_list)}')

with open('task5.txt', 'w', encoding='utf-8') as file:
    file.write(' '.join(map(str, random_list)))
