def division(divided, divider):
    """Возвращает частное от деления первого аргумента на второй

    Именованные аргументы:
    :param divided: делимое
    :param divider: делитель
    :return: <class 'dict'> {'ans': <class 'str'>, 'errorMes': <class 'str'>}
    """
    res = ''
    error = False
    try:
        divided = int(divided)
        divider = int(divider)
        res = divided / divider
    except ValueError:
        res = 'Ошибка во введенных значениях!'
        error = True
    except ZeroDivisionError:
        res = 'Деление на 0 недопустимо!'
        error = True
    return {'ans': res, 'errorMes': error}


while True:
    num1 = input('Введите первое число: ')
    num2 = input('Введите второе число: ')
    result = (division(num1, num2))
    print(result.get('ans'))
    if not result.get('errorMes'):
        break
