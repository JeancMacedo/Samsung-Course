def fib1(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b
N = int(input("Insira um número: "))
print(fib1(N))
print(2*"*************")

def fib2(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b
N = int(input("Insira um número: "))
print(fib2(N))
print(2*"*************")

def fib3(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b
N = int(input("Insira um número: "))
print(fib3(N))
print(2*"*************")

def fib4(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b
N = int(input("Insira um número: "))
print(fib4(N))