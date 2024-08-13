s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']

shortest_string = s_list[0]


for s in s_list:
    if len(s) < len(shortest_string):
        shortest_string = s

print(f"A string mais curta é: {shortest_string}")