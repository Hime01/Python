rating = [9, 5, 3, 2, 1]

user_numb = int(input(f'Введите число, чтобы добавить в рейтинг {rating}: '))
index = 0
for el in rating:
    if user_numb <= el:
        index += 1
    else:
        break
rating.insert(index, user_numb)

print(f'Измененный рейтинг: {rating}')
