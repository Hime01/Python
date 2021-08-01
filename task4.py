user_numb = int(input('Введите число, а я выдам самую большу цифру из него: '))

divider = 10
numb = user_numb % divider
while user_numb / divider > 0:
    user_numb = int(user_numb / divider)
    next_numb = int(user_numb % divider)
    if numb < next_numb:
        numb = next_numb

print(numb)
