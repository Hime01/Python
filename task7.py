import json

with open('text_7.txt', 'r', encoding='utf-8') as file:
    line_list = file.readlines()

# лепим удобный словарь
dict_firms = {}
for line in line_list:
    earnings, expenses = int(line.split()[2]), int(line.split()[3])
    dict_firms[line.split()[0]] = {'earnings': earnings, 'expenses': expenses, 'profit': earnings - expenses}

print(dict_firms)

# показываем прибыль каждой компании (если не убытки)
for firm in dict_firms:
    if dict_firms[firm]["profit"] > 0:
        print(f'Прибыль фирмы "{firm}" = {dict_firms[firm]["profit"]}')

# считаем среднюю прибыль
firms_profit = [obj['profit'] for obj in dict_firms.values() if obj['profit'] > 0]
average_profit = sum(firms_profit) / len(firms_profit)
print(f'Средняя прибыль всех компаний (исключая компании с убытком): {average_profit}')

# финальный список для json
firm_profit_dict = {firm: dict_firms[firm]["profit"] for firm in dict_firms}
final_list = [firm_profit_dict, {'average_profit': average_profit}]
print(final_list)

with open('task7.json', 'w', encoding='utf-8') as file:
    json.dump(final_list, file)
