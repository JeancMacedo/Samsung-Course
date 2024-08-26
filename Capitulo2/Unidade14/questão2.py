itens = {"Café":7, "Caneta":3,"Copo de papel":2,
         "Leite":1, "Coca-Cola": 4,"Livro":5}
print(itens)
item = input(f'Informe o item desejado: ')
estoque = itens.get(item)
print(f'Nome do item: {item}, \nQuantidade disponivel no estoque: \
{estoque}.')