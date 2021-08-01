first_day = int(input('Введите количество км, которое спортсмен пробежал в первый день: '))
final_km = int(input('Введите количество км, которое спортсмен должен достичь: '))
print('Я посчитаю количество дней, за которое спортсмен добьется этого результата, улучшая его на 10% каждый день.')

increase_k = 0.1
distance = first_day
day = 1
print(f'День {day}: {round(distance, 2)}')
if distance < final_km:
    while distance <= final_km:
        distance = distance + distance * increase_k
        day += 1
        print(f'День {day}: {round(distance, 2)}')

print(f'Спортсмен достигнет результата не менее {final_km} км на {day}-й день')
