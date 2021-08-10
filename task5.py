def my_sum():
    sum = 0
    while True:
        user_list = input('Введите числа через пробел, и я покажу их сумму. Для выхода введите q: ').split()
        for num in user_list:
            if num.lower() == 'q':
                return sum
            else:
                try:
                    num = float(num)
                    sum += num
                except ValueError:
                    print('Для выхода введите q.')
        print(f'Сумма введенных чисел с учетом предыдущих итераций = {round(sum)}')

print(f'Финальная сумма {round(my_sum())}. Выхожу из программы.')
