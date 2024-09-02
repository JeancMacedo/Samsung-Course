def media3(a, b, c):
    return (a + b + c) / 3

# Função para calcular o valor máximo de três números
def max3(a, b, c):
    return max(a, b, c)

# Função para calcular o valor mínimo de três números
def min3(a, b, c):
    return min(a, b, c)

a, b, c = map(int, input("Digite três números: ").split())

print(f"O valor médio de {a}, {b}, {c} é {media3(a, b, c)}")
print(f"O valor máximo de {a}, {b}, {c} é {max3(a, b, c)}")
print(f"O valor mínimo de {a}, {b}, {c} é {min3(a, b, c)}")

