def my_func(arg1, arg2, arg3):
    my_list = [arg1, arg2, arg3]
    sort = sorted(my_list)
    sort.reverse()
    return sum(sort[slice(2)])


arg_1 = input('Число 1: ')
arg_2 = input('Число 2: ')
arg_3 = input('Число 3: ')
try:
    arg_1, arg_2, arg_3 = int(arg_1), int(arg_2), int(arg_3)
    print(my_func(arg_1, arg_2, arg_3))
except ValueError:
    print('Нужны были циферки :(')
