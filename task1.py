from sys import argv

name, hours, salary, premia = argv
try:
    hours, salary, premia = float(hours), float(salary), float(premia)
    if hours <= 0 or salary <= 0 or premia <= 0:
        result = 'Значения не могут быть меньше или равны 0'
    else:
        result = round(hours * salary + premia, 4)
except ValueError:
    result = 'Значениями могут быть только цифры'

print(argv)
print(result)