with open('task2.txt', 'r', encoding='utf-8') as file:
    line_list = file.readlines()
    for numb, line in enumerate(line_list, 1):
        print(f'Строка {numb}. Содержимое - "{line.strip()}." Количество слов - {len(line.split())}')
