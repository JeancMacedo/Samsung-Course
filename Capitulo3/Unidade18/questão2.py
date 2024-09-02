def potencia_recursiva(x, n):
    if n == 0:
        return 1
    return x * potencia_recursiva(x, n-1)

x = int(input("Informe o valor de x: "))
n = int(input("Informe o valor de n: "))
resultado = potencia_recursiva(x,n)
print(f'{x} elevado a {n} é {resultado}')
