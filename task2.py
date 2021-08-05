my_list = input('Введите элементы списка через пробел: ').split()

print(f'Начальный список: {my_list}')

for i in range(0, len(my_list) - 1, 2):
    print(f'итерация i = {i}')
    print(f'my_list[i] = {my_list[i]}, my_list[i+1] = {my_list[i+1]}')
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

print(f'Финальный список список: {my_list}')