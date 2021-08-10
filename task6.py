def only_latin(sentence):
    if sentence != sentence.lower():
        return 'Можно вводить только слова в нижнем регистре!'
    word_list = sentence.split()
    latin_list = []
    not_latin = False
    for word in word_list:
        for char in word:
            if ord(char) < 97 or ord(char) > 122:
                not_latin = True
                break
        if not_latin:
            not_latin = False
            continue
        latin_list.append(word.capitalize())
    return " ".join(latin_list)


print(only_latin(input('Введите предложение в нижнем регистре, я выведу все слова на латинице и с большой буквы: ')))

# nice авп ъghj jапро hjjпаро вапрghgh cool
