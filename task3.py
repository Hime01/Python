with open('text_3.txt', 'r', encoding='utf-8') as file:
    line_list = file.readlines()
    employees = {line.split()[0]: float(line.split()[1]) for line in line_list}
    print(employees)
    less_twenty = [emp for emp in employees if employees.get(emp) < 20000]
    print(f'Сотрудники, чей оклад меньше 20 тысяч: {", ".join(less_twenty)}')
    average = sum(employees.values()) / len(employees.values())
    print(f'Средняя величина дохода сотрудников: {round(average, 4)}')
