def is_palindrome(n):
    n_str = str(n)
    return n_str == n_str[::-1]

n = int(input('Digite um número: '))
if is_palindrome(n):
    print(f'{n} é um número palíndromo.')
else:
    print(f'{n} não é um número palíndromo.')

n1 = (input('Digite um número: '))
n1 = n1[::-1]
print(f'n1: {n1}') 