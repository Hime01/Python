rus_eng = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('text_4.txt', 'r', encoding='utf-8') as file:
    line_list = file.readlines()

rus_lines = [line.replace(line.split(' - ')[0], rus_eng[line.split(' - ')[0]]) for line in line_list]

with open('task4.txt', 'w', encoding='utf-8') as result:
    result.writelines(rus_lines)
