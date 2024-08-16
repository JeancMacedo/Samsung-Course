lista = [(), (1,), [], 'abc', (), (), (1,), ('a',), ('a', 'b'), ((),), '']

# Remover tuplas, strings e listas vazias
lista_filtrada = [item for item in lista if item != () and item != '' and item != [] or item == ((),)]

# Exibir a lista sem os elementos vazios
print(f"A lista sem os elementos vazios: {lista_filtrada}")