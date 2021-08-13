from functools import reduce

my_list = [numb for numb in range(100, 1001) if numb % 2 == 0]
print(my_list)


def reducer_sum(el1, el2):
    #print(f'el1 = {el1}, el2 = {el2}')
    return el1 * el2

print(reduce(reducer_sum, my_list))
