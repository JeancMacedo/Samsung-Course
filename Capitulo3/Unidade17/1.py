def print_star(n):
    for _ in range(n):
        print('*****************')
print_star(4) #4 é o valor do argumento para o números de linhas com asterisco
print(f'-='*20)

def print_hello(n):
    print('Hello ' * n)
print('Imprime olá duas vezes')
print_hello(2)
print('Imprime olá 3 vezes')
print_hello(3)
print('Imprime olá 4 vezes')
print_hello(4)
print(f'-='*20)

def print_sum(a, b):
    resultado = a + b
    print('A soma de a e b é ', resultado)
print_sum(10, 20)
print_sum(100, 200)
print(f'-='*20)

def greet(*nomes):
	for nome in nomes:
		print('Olá ', nome, '!')
greet('A', 'B', 'C') #3 argumentos
greet('James', 'Thomas') #2 argumentos
print(f'-='*20)

def foo(*args):
    print('Número de argumentos: ', len(args))
    print('Argumentos: ', args)
foo(10, 20, 30)
print(f'-='*20)

def sum_nums(*numbers):
    result = 0
    for n in numbers:
        result += n
    return result
print(sum_nums(10, 20, 30)) #Imprime a soma dos argumentos 10, 20 e 30
print(sum_nums(10, 20, 30, 40, 50)) #Imprime a soma dos argumentos 10, 20, 30, 40 e 50
print(f'-='*20)

def print_star(n = 1):  # O parâmetro n tem o valor padrão de 1
	for _ in range(n):
		print('**********')
print_star() # Executa sem erros, mesmo sem argumetos.
print(f'-='*20)

def print_star(n = 1):  # O parâmetro n tem o valor padrão de 1
	for _ in range(n):
		print('**********')
print_star(2) # Como o valor do argumento é 2, o parâmetro padrão n=1 não é realizado
print(f'-='*20)

def div(a, b=2):
	return a/b
print('div(4) = ', div(4))
print('div(6/3) = ', div(6,3))
print(f'-='*20)

def div(a = 1, b = 2):
	return a/b
print('div() = ', div())
print('div(4) = ', div(4))
print('div(6, 3) = ', div(6, 3))
print(f'-='*20)

def get_root(a, b, c):
    r1 = (-b +(b**2 - 4 * a * c)) ** 0.5 / (2 * a)
    r2 = (-b -(b**2 - 4 * a * c)) ** 0.5 / (2 * a)
    return r1, r2
# Ao chamar uma função, use um valor constante como argumento
# Retornar o valor do resultado usando o resultado 1 e o resultado 2
result1, result2 = get_root(1, 2, -8)
print('O resultado é ', result1, ' ou ', result2)
print(f'-='*20)

result1, result2 = get_root(-5, 2, 1)
print('O valor do resultado é ', result1, ' ou ', result2)
print(f'-='*20)

result1, result2 = get_root(a = 1, b = 2, c = -8)
print('O valor do resultado é ', result1, ' ou ', result2)
print(f'-='*20)

def get_sum(a, b):
    result = a + b
    return result
n1 = get_sum(10, 20)
print('A soma de 10 e 20 = ', n1)
n2 = get_sum(100, 200)
print('A soma de 100 e 200 = ', n2)
print(f'-='*20)

def get_root(a, b, c):
    r1 = (-b +(b**2 - 4 * a * c) ** 0.5 / (2 * a))
    r2 = (-b -(b**2 - 4 * a * c) ** 0.5 / (2 * a))
    return r1, r2 # Devolve 2 raízes: r1 e r2 da equação quadrática
# Ao chamar uma função, use um valor constante como argumento
# Retornar o valor do resultado usando o resultado 1 e o resultado 2
result1, result2 = get_root(1, 2, -8)
print("O resultado é ", result1, ' ou ', result2) # result1 e result2 recebem o valor de r1 e r2