

def calc_digit(n):
    def final(digit):
        return digit**n
    return final
num_list = []
for num in range(1, 6):
    num_list.append(calc_digit(num))
    print(num_list[num - 1](num))