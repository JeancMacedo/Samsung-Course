def func1(a):
    # Função aninhada para encontrar números divisíveis por 5
    def func2(a):
        result1 = []
        for i in a:
            if i % 5 == 0:
                result1.append(i)
        return result1

    # Função aninhada para encontrar números divisíveis por 7
    def func3(a):
        result2 = []
        for i in a:
            if i % 7 == 0:
                result2.append(i)
        return result2
    
    # Chamando as funções func2 e func3
    divisiveis_por_5 = func2(a)
    divisiveis_por_7 = func3(a)
    
    # Combinando os resultados, removendo duplicatas e ordenando
    result = list(set(divisiveis_por_5 + divisiveis_por_7))
    return sorted(result)

# Lista de 0 a 100
lst = list(range(101))

# Chamando a função func1 e imprimindo o resultado
result = func1(lst)
print(result)
