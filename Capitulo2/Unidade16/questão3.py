minha_lista = [(1, 2), (4, 5), (4, 2), (3, 1), (9, 4)]

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

tupla_ab = (a, b)
tupla_ba = (b, a)

if tupla_ab in minha_lista:
    posicao_ab = minha_lista.index(tupla_ab)
    print(f'Há {tupla_ab} na posição {posicao_ab}')
elif tupla_ba in minha_lista:
    posicao_ba = minha_lista.index(tupla_ba)
    print(f'Não há {tupla_ab} mas há {tupla_ba} na posição\
 {posicao_ba}')
else:
    print(f"Não há {tupla_ab} e nem {tupla_ba}")
