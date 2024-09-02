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

print(f'-='*20)

print(f'-='*20)

print(f'-='*20)

print(f'-='*20)

print(f'-='*20)

print(f'-='*20)

print(f'-='*20)