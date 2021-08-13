given_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [given_list[i] for i in range(1, len(given_list)) if given_list[i] > given_list[i - 1]]
print(new_list)
