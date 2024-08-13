# Definindo a lista
lst = [5, 6, 3, 9, 2, 12, 3, 8, 7]

# Bubble Sort para garantir que o maior valor esteja no final
for i in range(len(lst) - 1):
    for j in range(len(lst) - 1 - i):
        if lst[j] > lst[j + 1]:
            # Troca de valores usando tupla
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print(lst)