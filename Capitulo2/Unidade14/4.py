"""
Vamos atualizar o programa para gerenciar o 
inventário de lojas de conveniência que resolvemos em 
codificação em papel. Em outras palavras, 
adicionar código para aumentar ou diminuir o estoque.
Além disso, fazer menus simples, como consulta de 
inventário, armazenagem e expedição.
"""

itens = {"Café": 7,
         "Caneta": 3,
         "Copo de papel": 2, 
         "Leite": 1,
         "Coca-Cola": 4,
         "Livro": 5}
while True:
    print("Selecione menu:\n\n\
\t1)Verificar estoque;\n\
\t2)Armazenar;\n\
\t3)Liberação;\n\
\t4)Saída.")
    entrada_de_item = input('Informe a opção: ')
    if entrada_de_item == 1:
        print(itens)
    elif entrada_de_item == 2:
        print()