list_array = [] #Cria lista vazia

for i in range(3):    
    line = []
    for j in range(2):
        line.append(0)
    list_array.append(line)
print(list_array)

print('\n')

list_array = [[0] * 2 for i in range(3)]
print(list_array)

print("\n")

list_array = [[0 for j in range(2)] for i in range(3)]
print(list_array)

print("\n")

list_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
i = 0
print(len(list_array))
while i < len(list_array):  
    a, b, c = list_array[i]
    print(a, b, c)    
    i += 1

print("\n")

list1 = [[0] * i for i in [1, 2, 3, 4, 5]]
print(list1)

print("\n")

for i in list1:
    for j in i:
        print(j, end = ' ')
    print()

print("\n")

list1 = [[10 * i] * i for i in [1, 2, 3, 4, 5]]
print(list1)

print("\n")

list1[0].append(99)
list1[1].append(77)
print(list1)

print("\n")

f = open('hello.txt', 'w')
f.write('hello world!')
f.close()

print("\n")

f = open('hello.txt',  'w')	    #Abrir arquivo
f = open('hello.txt',  'wt')	#Abrir arquivo em texto
f = open('hello.txt',  'wb')	#Abrir arquivo em binário
f = open('hello.txt',  'r+t')	#Modo de leitura/escrita de texto

print("\n")

f = open('hello.txt',  'w+t')	#Modo de escrita/leitura de texto
f = open('hello.txt',  'a+t')	#Adicionar texto
f.write('Hello World!\n')	#Escreva no arquivo hello.txt
f.write('Love of my life, you\'ve hurt me\n')
f.write("You've broken my heart and now you leave me\n")
f.write('Love of my life, can\'t you see?\n')
f.close()	#Fechar arquivo

print("\n")

'''Se 5 é dado como um parâmetro do método f.read, ele lê 5 caracteres do arquivo e os devolve em uma string.
Apenas cinco caracteres "Hello" são impressos.
f = open('hello.txt', 'r')	#Abrir arquivo
s = f.read(5)	#Leia cinco letras do arquivo hello.txt
print(s)	#Imprimir o conteúdo do arquivo
f.close()	#Fechar arquivo
'''
print("\n")
f = open('hello. txt', 'r+') #Abrir arquivo
S = f.readline() #Leia a primeira linha do arquivo.
print(S, end = '') #imprimir a linha
S = f.readline()  #Leia a segunda linha do arquivo.
print(S, end = '') #imprimir a linha
f. close() #Fechar arquivo

print("\n")
f = open('hello.txt', 'a+')	#Abrir arquivo
f.write('This will be appended.\n')
f.write('This too.\n')
f.close()

print("\n")

f = open('hello.txt', 'a+')	#Abrir arquivo
s = f.read()	#Ler o arquivo hello.txt
print(s)	#Imprimir o conteúdo do arquivo
f.close()

print("\n")

f = open('data5.txt', 'w')#Abrir arquivo em modo escrita
for _ in range(5):
    n = input("Insira o número inteiro: ")	#Escreva a entrada como string    f.write(n)    f.write('\n')	# Escreva o valor e a quebra de linha
f.close()	# fechar arquivo

print("\n")

with open('hello.txt', 'w') as f:	# abrir e fechar automaticamente o arquivo no final do bloco
    f.write('Hello World!')	# escrever no arquivo hello.txt

print("\n")

f = open('hello.txt', 'w')	#arquivo aberto
try:
    f.write('Hello World!')	#escrever no arquivo hello.txt
finally:
    f.close()	#fechar arquivo

print("\n")
