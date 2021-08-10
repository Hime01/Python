def my_func(numb, power):
    try:
        numb = float(numb)
        power = int(power)
    except ValueError:
        return 'Возводимое должно быть действительным положительным числом, а степень - целым отрицательным.'
    if power >= 0 or numb < 0:
        return 'Возводимое должно быть действительным положительным числом, а степень - целым отрицательным.'
    result = 1
    for i in range(abs(power)):
        result = result / numb
    return result


while True:
    res = my_func(input('Введите действительное положительное число, его будем возводить в степень: '), input('Введите целое отрицательное число, это степень: '))
    print(res)
    if not isinstance(res, str):
        break
