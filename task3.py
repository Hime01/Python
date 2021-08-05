month_list = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]  # список времен года, внутри которых список месяцев
month_dict = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}

while True:
    user_month = int(input('Введите номер месяца: '))
    if user_month < 1 or user_month > 12:
        print(f'{user_month} не может быть номером месяца.')
    else:
        print('Решение через list:')
        for season in month_list:
            for month in season:
                if month == user_month:
                    season_numb = month_list.index(season)
                    if season_numb == 0:
                        text = 'зиме'
                    elif season_numb == 1:
                        text = 'весне'
                    elif season_numb == 2:
                        text = 'лету'
                    else:
                        text = 'осени'
        if not text:
            print('Что-то поломалося, давайте заново.')
            continue
        print(f'Месяц {user_month} относится к {text}.')

        print('Решение через dict:')
        for value in month_dict.values():
            if value.count(user_month) != 0:
                for key in month_dict.keys():
                    if month_dict[key] == value:
                        season_dict = key
        if not season_dict:
            print('Что-то поломалося, давайте заново.')
            continue
        print(f'Месяц {user_month} - это {season_dict}.')
        break
