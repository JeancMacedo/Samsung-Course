diarias = (100, 121, 120, 130, 140, 120, 122, 123, 190, 125)
print(len(diarias))
num = 0
for i in range(1, len(diarias)):
    if diarias[i] < diarias[i - 1]:
        num += 1
print(num)
