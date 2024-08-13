s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']

maior_string = s_list[0]

for s in s_list:
    if len(s) > len(maior_string):
        maior_string = s

print(f"A string mais curta é: {maior_string}")