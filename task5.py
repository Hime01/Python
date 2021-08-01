earnings = int(input('Введите значение выручки: '))
expenses = int(input('Введите значение издержек: '))

diff = earnings - expenses

if diff < 0:
    print(f'Фирма отработала с издержками в размере {diff * -1}')
elif diff == 0:
    print('Издержки и выручка равны')
else:
    print(f'Фирма отработала с прибылью в размере {diff}')
    rentable = int(earnings / expenses)
    print(f'Рентабельность выручки: {rentable}')
    numb_workers = int(input('Сколько сотрудников работает в фирме? '))
    earnings_worker = int(diff / numb_workers)
    print(f'Прибыль фирмы в расчете на одного сотрудника: {earnings_worker}')

# округляю значения, потому что слышала на вебинаре, что просят делать именно так
