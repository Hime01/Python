my_list = input('Введите несколько слов через пробел: ').split()

for i, item in enumerate(my_list, 1):
    if len(item) > 10:
        item = item[:10]
    print(f'{i}) {item}')