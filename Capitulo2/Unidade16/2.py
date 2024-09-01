"""
Se a ordem não for importante : Set

Definição de conjunto

O conjunto usado em Python também é similar ao conjunto de matemática e, ao contrário das tuplas, é um tipo de dado sem ordem.
Em particular, a duplicação de itens com o mesmo valor não é permitida, e várias operações de conjunto, como interseção, união, diferença de conjunto e diferença simétrica de conjunto podem ser realizadas.
"""
numbers = {2, 1, 3} # tipo de dados do conjunto consistia em 3 números
print(numbers)
print(f'=-'*20)
a_set = {1, 5, 4, 3, 7, 4} #fazer um conjunto de seis itens
len(a_set) #número do item é 5 excluindo a duplicação

max(a_set) #o maior número dentro do item é 7

min(a_set) #o menor número dentro do item é 1

sorted(a_set) #fazer lista organizando os itens, sem duplicação

sum(a_set) #Como o número duplicado só é usado uma vez, a soma é 20
"""
Se a ordem não for importante : Set

Funções lógicas computacionais aplicáveis a um conjunto

As operações lógicas que podem ser aplicadas aos dados com múltiplos itens incluem todas e quaisquer funções.
Esta função retorna de forma abrangente o resultado da avaliação booleana para cada item de dados dado como um fator.
Vamos fazer um conjunto de seis itens, como mostrado abaixo. Aplique várias funções.
"""
a_set = { 1, 0, 2, 3, 3}
print(all(a_set), any(a_set)) #O a_set é todo verdade? Existe - em a_set?
print(f'=-'*20)
"""
'All' avalia cada um dos itens de dados repetíveis dentro de um tipo booleano e retornam verdadeiros se tudo for verdade. 
Se um é falso, ele retorna falso.
'Any' avalia cada um dos itens de dados repetíveis na forma de um booleano e retorna verdadeiro independentemente do outro valor, se algum for verdadeiro.
Se tudo é falso, o retorno é falso.
Se a ordem não for importante : Set

Aliquota e maior fator comum e pensamento de programação

Vamos pensar em como obter a alíquota de dois inteiros.
A alíquota de 10 pode ser 1, 2, 5 e 10, das quais 1 e 2 e 5 excluindo suas próprias 10 são chamadas de alíquota verdadeira. 
Faça uma lista como segue, e divida dez com dois, três, quatro, cinco... Divida todos os números até 9 e verifique se os valores restantes são zero, e se for o caso, coloque-os na lista.
"""
num = 10
divisors = []
for i in range(2, num) :
	if num % i == 0:
         divisors.append(i)
print(num,' e sua verdadeira aliquota: ', divisors)
print(f'=-'*20)
"""
Linha 4, 5, 6

i aumenta em 1 de 2 e passa para 9. A razão para começar com 2 é para obter a verdadeira alíquota.
Dividir num por i e adicioná-lo à lista porque é um verdadeiro divisor se o restante for zero.
Você pode ver os números de aliquotas 2 e 5 de 10.
Se a ordem não for importante : Set

Aliquota e maior fator comum e pensamento de programação

Para usar este código para encontrar o divisor máximo comum de 48 e 60, encontre o divisor verdadeiro de 48 e 60, e depois encontre o maior deles.
Para este fim, vamos declarar um conjunto vazio de tipos de dados de get_divisors1 e divisors2 e acrescentar um valor a este conjunto onde o num % i se torna zero.
"""
num1 = 48
divisors1 = set()

for i in range(2, num1):
 if num1 % i == 0:
    divisors1.add(i)
print(num1,'s true aliquot :', divisors1)

num2 = 60
divisors2 = set()

for i in range(2, num2):
  if num2 % i == 0:
    divisors2.add(i)
print(num2,'s true aliquot : ', divisors2)
print(f'=-'*20)
"""
Se a ordem não for importante : Set

Aliquota e maior fator comum e pensamento de programação

Agora vamos encontrar um divisor comum entre estes divisores.
E use a função 'max' para encontrar o maior desses valores. 
É claro que existe o método MDC de obter dois divisores 
máximos mais rápido que este método, mas seria uma forma 
programática de pensar para encontrar soluções através de 
um processo passo-a-passo de resolução de problemas como este.
"""
print(divisors1.intersection(divisors2))
print(num1, num2, 'o divisor máximo é: ', max(divisors1.intersection(divisors2)))
print(f'=-'*20)
"""
Linha 2

Encontre a intersecção dos elementos A e B e então imprima o maior valor usando a função max.
O divisor máximo comum de 40 e 60, é o 12 e ele é impresso.
Agregação usando a função Zip

As características da função zip e os tipos de dados repetíveis

Tipos de dados tais como listas, dicionários, conjuntos e tuplas são chamados de tipos de dados repetíveis.
Quando vários tipos de dados repetíveis são inseridos, a função que retorna o iterador tupla, combinando-os, é a função zip.
A função zip pode receber vários tipos de dados que podem ser repetidos, como mostrado abaixo. Isto é chamado de agregação.

Agregação usando a função Zip

Exemplo de código usando a função zip
"""
empty_iterator = zip()
result = set(empty_iterator)
print(result)
"""
set()

Se o fator não for transferido, a função zip retorna um iterador de espaço.
Quando um fator de tipo de dado repetível entra, a função zip retorna um repetidor para uma tupla.
Cada elemento desta tupla é transferido um valor obtido a partir dos dados transferidos para o fator.
Quando n fatores do tipo de dados repetíveis entram, o iterador tupla se torna um iterador tupla com tantas tuplas quanto o número de fatores.
Aqui, o i-ésimo elemento, a tupla, é composto de i-ésimo elemento de cada fator do tipo de dados repetíveis que passou para o fator.
"""
print(f'=-'*20)
a = [10, 20, 30] #lista a
b = ('dez', 'vinte', 'trinta') #tupla b
for val in zip(a, b): #print tupla criada pela agregação da lista a e tupla b
    print(val)
print(f'=-'*20)
"""
Agregação usando a função Zip

Precauções para o uso da função zip

Quando um fator de tipo de dado repetível é transferido para a função zip, ele aparece como um objeto tupla ('a',), e não como 'a'.

Se a lista com uma string como elemento for inserida na função zip como dados repetíveis.
Note que o elemento resultante é um tupla, portanto aparece como um tupla ('a',) com um elemento chamado 'a', não apenas 'a' porque é um tupla.
"""
lst = ['a', 'b', 'hello', 'this']
my_iterator = zip(lst)
result = set(my_iterator)
print(result)
print(f'=-'*20)
print(f'=-'*20)
print(f'=-'*20)
print(f'=-'*20)
print(f'=-'*20)
