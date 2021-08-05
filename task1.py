my_list = [
    51, 1.5, 4 - 1j, 'Capybara', [2, '123123', None],
    (2, '123123', None), {2, '123123', None}, {'first': 1, 'second': 2},
    False, b'text', None, ValueError
]

for numb, item in enumerate(my_list, 1):
    print(f'{numb}. {item} - {type(item)}')
