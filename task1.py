with open('task1.txt', 'w', encoding='utf-8') as file:
    while True:
        text = input('Введите текст: ')
        if not text:
            break
        file.write(f'{text}\n')
