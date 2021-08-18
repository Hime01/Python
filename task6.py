with open('text_6.txt', 'r', encoding='utf-8') as file:
    line_list = file.readlines()

dict_subjects = {}

for line in line_list:
    subject, hours = line.split(':')
    symbs_arr = [symb for symb in hours if symb == ' ' or symb.isdigit()]
    filtered_hours = ''.join(symbs_arr).split()
    hours_sum = sum(map(int, filtered_hours))
    dict_subjects[subject] = hours_sum

print(dict_subjects)
