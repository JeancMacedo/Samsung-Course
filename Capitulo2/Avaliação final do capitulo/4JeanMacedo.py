# Matriz bidimensional
a = [[1, 2], [3, 4], [5, 6]]

# Nova matriz unidimensional
flattened = []

# Usando um for loop para percorrer a matriz bidimensional e 
# adicionar os elementos à matriz unidimensional
for sublist in a:
    for item in sublist:
        flattened.append(item)

# Imprimindo a matriz unidimensional
print(flattened)