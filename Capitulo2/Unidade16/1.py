'''
Fazendo conjunto vazio
set0 = set() 


Fazendo um conjunto básico	
set1 = {1, 2, 3, 4}


Fazendo conjunto a partir da tupla	
n_tuple = (1, 2, 3, 4)
set2 = set(n_tuple)


Fazendo conjunto a partir da lista	
n_list = [1, 2, 3, 4]
set3 = set(n_list)
'''

days_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']  #lista
days_set = set(days_list)  #fazendo conjuntos a partir da lista
print(days_set)
print(f"=-="*20)
fruits_tuple = ('apple', 'orange', 'watermelon') #tuple
fruits_set = set(fruits_tuple) #fazendo conjuntos a partir do tuple
print(fruits_set)
print(f"=-="*20)
h_str = 'hello' #string
h_set = set(h_str) #Fazendo conjuntos a partir da string
print(h_set) #O conjunto não permite a duplicação do string 'l
print(f"=-="*20)
numbers = {2, 1, 3}
if 1 in numbers: #verificar se 1 está nos números definidos
    print("1 está no conjunto")
print(f"=-="*20)
numbers = {1, 2, 3}
numbers.add(4)
print(numbers)
numbers.remove(4)
print(numbers)
print(f"=-="*20)
s1 = {1, 2, 3, 4, 5, 6}
s2 = {4, 5, 6, 7, 8, 9}
print(s1 | s2) #Encontrar união
print(s1 & s2) #Encontrar interseção
print(s1 - s2) #Encontrar diferença de conjunto
print(s1 ^ s2) #Encontrar diferença simétrica do conjunto
print(f"=-="*20)
s1 = {1, 2, 3, 4, 5, 6}
s2 = {4, 5, 6, 7, 8, 9}
print(s1.union(s2))#Encontrar união
print(f"=-="*20)
print(s1.intersection(s2)) #Encontrar interseção
print(f"=-="*20)
print(s1.difference(s2)) #Encontrar diferença de conjunto
print(f"=-="*20)
print(s1.symmetric_difference(s2)) #Encontra a diferença simétrica do conjunto
print(f"=-="*20)
s1 = {1, 2, 3, 4, 5, 6}
s2 = {4, 5, 6, 7, 8, 9}
s3 = {5, 6, 9, 10, 11}
print ("União: ",s1 & s2 & s3) # União entre s1, s2 e s3
5, 6
print ("Diferença: ", s1 - s2 - s3) # Subtrair elementos de s2 e s3 de s1
1, 2, 3
print(f"=-="*20)


"""
Os métodos relacionados com o conjunto e o que eles fazem

métodos	| papel
add(x)	| Acrescentar o elemento x ao conjunto.
discard(x)	| Eliminar o elemento x do conjunto.
clear | Excluir todos os elementos do conjunto.
union(s) | Encontrar união com conjunto s. O mesmo que o operador |. 
difference(s) | Encontrar diferença de conjunto com conjunto s. O mesmo que o operador -.
intersection(s) | Encontrar o cruzamento do conjunto com o conjunto s. O mesmo que o operador &.
symmetric_difference(s) | Encontrar a diferença simétrica do conjunto com o conjunto s. O mesmo que o operador ^.
issubset(s)	| Encontrar o id do subset 's' que é um subconjunto. Return True/False.
issuperset(s) | Encontrar o id superset 's' que é um superconjunto. Return True/False.
isdisjoint(s) | Encontrar elementos que não são comuns entre os conjuntos. Return True/False.
"""
print(f"=-="*20)
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3} # é subconjunto do s1
s3 = {1, 2, 6} #não é o subconjunto do s1

print(s2.issubset(s1)) #método perguntando se s2 é subconjunto de s1

print(s3.issubset(s1)) #método perguntando se s3 é subconjunto de s1

print(s1.issuperset(s2)) #método perguntando se s1 é subconjunto de s2

print(s1.issuperset(s3)) #método perguntando se s1 é subconjunto de s3
print(f"=-="*20)
A = {1, 3} #elemento do conjunto A
B = {2, 4} #elemento do conjunto B
res = set()
for i in A:
    for j in B:
        res = res | {(i,j)} #conjunto de produtos com duplo loop for
        AxB = res #Conjunto de produtos AxB de A e B(não A*B)
print('A=', A)
print('B=', B)
print('AxB =', AxB) #imprimir o conjunto de produtos A e B
print(f"=-="*20)