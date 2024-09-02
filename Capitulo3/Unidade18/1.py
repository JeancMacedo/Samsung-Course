from timeit import * # importa todas as classes do método timeit

dic = {0:0, 1:1} # Declare um dicionário para memotização como variável global, dic = {0:0, 1:1} Chamando fibonacci_2(1) retorna 1, que é dic[1].

def fibonacci_2(n):
    if n in dic:
        return dic[n] # Se o dicionário já tem um resultado computado, ele retorna o resultado e não faz uma chamada recursiva.

    dic[n] = fibonacci_2(n-1) + fibonacci_2(n-2) # Se o dicionário não tiver resultado computado, a função faz uma chamada recursiva. O resultado da chamada é armazenado em um dicionário.

    return dic[n]

t2 = Timer('fibonacci_2(30)', 'from __main__ import fibonacci_2')
print('tempo de fibonacci_2(30) * 20: ', t2.timeit(number = 20), ' segundos')