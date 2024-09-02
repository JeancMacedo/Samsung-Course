"""
Processamento de strings
Várias funções e métodos de processamento de strings

Vamos mergulhar mais fundo nos métodos de strings que aprendemos na unidade 14.
Aprenda o método de contagem aplicável às strings.
Além disso, vamos obter o comprimento de uma string usando a função len.
O método de contagem de strings retorna o número de ocorrências de um substrato em uma string.
"""
birth = '1995.05.13' # Exemplo de data de nascimento
birth.count('.') # Exemplo de data de nascimento
Resultado: 2
"""
Além dos métodos mencionados acima, as funções embutidas também podem ser aplicadas às strings. A função len retorna o comprimento de uma string.
"""
birth = '1995.05.13'
print('Comprimento do birth: ', len(birth)) # Retornar o comprimento do nascimento da string
"""
Resultado: Comprimento do birth: 10

Processamento de strings usando funções incorporadas

Você pode usar as funções max e min para obter os maiores e menores caracteres. O critério de maior ou menor é baseado no valor do código Unicode.
Unicode é um sistema de código padrão da indústria para definir caracteres que podem ser usados em computadores.
A função ord pode obter o valor Unicode para um caractere, e o valor chr retorna o caractere correspondente ao valor Unicode de entrada.
"""
birth = '1995.05.13' # Exemplo de data de nascimento
max(birth)
"""
Resultado: '9'
"""
ord(max(birth)) # Retorna o valor Unicode de 9
"""
Resultado: '57'
"""
ord(min(birth)) # Retorna o valor Unicode do menor valor Unicode dentro de birth
"""
Resultado: '46'
"""
chr(57), chr(46) # Retorna o caractere correspondente aos valores Unicode 57 e 46
"""
Resultado: ('9', '.')

Vários métodos de strings

Aprenda vários métodos de strings e como utilizá-los.
"""
a = 'Eu amo python'
a.count('o') # Retorna o número de ocorrências do caractere 'o'.
"""
Resultado: 2

a.count('k') # Retorna o número d ocorrências do caractere 'k'.
Resultado: 0

a.find('o') # Retorna o índice que o caracter 'o' aparece
Resultado: 3

a.find('on') # Retorna o o índice com os caracteres 'on'.
Resultado: 11

a.startswith('E') # Retorna True, pois a string começa com o caractere 'e'.
Resultado: True

a.endswith('python') # Retorna True, pois a string termina com 'python'.
Resultado: True

Vários métodos de strings

Os métodos de string para letras maiúsculas e minúsculas
a = 'Eu Amo Python'
g = 'eu amo python'
h = 'EU AMO PYTHON'
a.upper() # Converte todas as letras em maiúsculas
Resultado: EU AMO PYTHON

h.lower() # Converte todas as letras em minúsculas
Resultado: eu amo python

a.swapcase() # Converte maiúsculas em minúsculas e vice-e-versa
Resultado: eU aMO pYTHON

a.istitle() # Retorna True se os primeiros caracteres de cada palavra forem maiúsculas
Resultado: True

Usando o módulo de string

Tente fatiar o alfabeto
Se a cadeia até 'ABCDE...YZ' é movida um caractere de cada vez, que método deve ser usado para criar uma cadeia como 'BCDEF...ZA'?
Neste caso, podemos resolver este problema com as seguintes operações simples de fatiagem e adição.
import string
src_str = string.ascii_uppercase
dst_str = src_str[1:] + src_str[:1]
print('dst_str = ',dst_str)
Resultado: dst_str = BCDEFGHIJKLMNOPQRSTUVXYZ

Linha 1, 2

Atribuir letras maiúsculas de A a Z a src_str.
Adicione [:1], a letra A, a [1:], a cadeia de caracteres de B a Z. Neste caso, src_str[1:] + src_str[:1] é usado para criar caracteres concatenados.
Usando o método de index

A posição da letra A em src_str pode ser solicitada com o método index.
Por outro lado, se n obtido usando este índice é procurado por dst_str como um índice, pode ser confirmado que a letra de dst_str correspondente à posição 'A' de src_str é 'B'.
n = src_str.index('A')
print('O índice de src_str = ', n)print('A posição do caractere \'A\' de src_str em dst_str =', dst_str[n])
Resultado:

O índice de src_str = 0

A posição do caractere 'A' de src_str em dst_str = B

Encontrar a solução de uma equação quadrática usando parâmetros
Soluções de equações quadráticas

Se os coeficientes da equação quadrática são a, b e c, respectivamente, a fórmula quadrática é a seguinte. Assumir que a não é zero aqui.
Digite os valores correspondentes a(a != 0), b, e c de acordo com a equação.
Vamos encontrar a solução quando os coeficientes forem a, b e c. Salve esta solução nas variáveis r1 e r2 e imprima-a.
def print_root(a, b, c):
    r1 = (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)
    print('A solução é ', r1, ' ou ', r2)

# Resolver equações quadráticas com diferentes valores de coeficientes
print_root(1, 2, -8)
print_root(2, -6, -8)
Resultado:

A solução é 2.0 ou -4.0

A solução é 4.0 ou -1.0

Recebe três argumentos passados externamente como parâmetros a, b e c, e realiza uma operação quadrática de fórmula no corpo funcional. Como resultado, é um código de função que emite r1 e r2.
O uso de funções torna o código muito mais conciso e fácil de usar.
Declaração de retorno múltiplo
Uma função que devolve a área e o perímetro de um círculo

Use o raio do círculo para encontrar a área e o perímetro do círculo.
A função circle_area_circum(radius) é implementada para receber um raio 10 como entrada e retornar dois valores, uma área e uma circunferência.
def circle_area_circum(radius):
    area = 3.14 * radius ** 2
    circum = 2 * 3.14 * radius
    return area, circum
Uma função que devolve a área e o perímetro de um círculo

As declarações de retorno que retornam dois ou mais valores são chamadas de declarações de retorno múltiplas.
Em declarações múltiplas de retorno, dois valores separados por uma vírgula são devolvidos como um tipo tupla.
def circle(r):
    pi = 3.14
    area = pi * r * r
    circ = 2 * pi * r
return area, circ
ar,ci = circle(10)
print('A area do círculo de raio {} é {:.1f}, e a circunferência é
{:.1f}'.format(10, ar, ci))
Resultado: A area do círculo de raio 10 é 314,0, e a circunferência é 62,8

Linha 1, 7-8

No código acima, a função circum_area_circum recebe um raio como parâmetro e retorna dois valores correspondentes à área e circunferência do círculo.
Fora da função da Linha 7-8, a função circum_area_circum é chamada e o resultado do cálculo é armazenado na área das variáveis e as circunscreve e imprime.
Variável Global
O conceito de variáveis globais

Aprenda o termo variável global.
Uma variável global é uma variável declarada fora de uma função e está disponível para toda a área de código.
Se você olhar para o código e diagrama abaixo, você pode ver que as variáveis a e b são chamadas e usadas tanto no arquivo de script com o código Python quanto na função print_sum.
def print_sum():
    result = a + b
    print('print_sum() da função: a soma de ', a, ' e ', b, 'é: ',result)
a = 10
b = 20
print_sum()
result = a + b
print('print_sum() fora da função: a soma de ', a, ' e ', b, 'é: ',result)
Resultado:

print_sum() da função : a soma de 10 e 20 é 30

print_sum() fora da função: a soma de 10 e 20 é 30

4.1. The concept of global variables img

O conceito de variáveis globais

Variáveis Globais e Código de Exemplo
E se uma variável global definida fora de uma função for alterada dentro da função?
Dê uma olhada no código abaixo. Dentro da função print_sum, a e b foram modificadas para 100 e 200 dentro da função, mas por que não foram modificadas fora da função?
def print_sum():
    a = 100
    b = 200
    result = a + b
    print('print_sum() da função: a soma de ', a, ' e ', b, 'é: ',result)
a = 10
b = 20
print_sum()
Resultado: print_sum() da função : a soma de 100 e 200 é 300

O conceito de variáveis globais

Mudança de variável global e código a verificar
Alterar os valores das variáveis globais a e b dentro da função e executar o código para verificar os valores
def print_sum():
    a = 100 # Criar novas variáveis a e b referentes a 100, 200
    b = 200
    result = a + b
    print('print_sum() da função: a soma de ', a, ' e ', b, 'é: ',result)
a = 10 # Criar variáveis a e b referenciando a 10, 20
b = 20
print_sum()
result = a + b
print('print_sum() fora da função: a soma de ', a, ' e ', b, 'é: ',result)
Resultado:

print_sum() da função : a soma de 100 e 200 é 300

print_sum() fora da função: a soma de 10 e 20 é 30

Após executar o print_sum, adicionar novamente a e b fora da função, atribuí-lo ao resultado e imprimir o resultado.
As a e b foram mudadas para 100, 200 dentro da função foram mudadas fora da função?
Se você verificar o resultado, você pode ver que os valores a e b dentro da impressão_sum são diferentes dos valores a e b fora da função.
O conceito de variáveis locais

Resultados e interpretação do código anterior

A declaração de atribuição Python é: a = 100, b = 200
Dentro de uma função, esta declaração de atribuição cria uma variável local.
As variáveis globais a e b referem-se aos valores globais 10 e 20.
Dentro da função print_sum, a e b referem-se aos novos objetos 100 e 200.
4.2. The concept of local variables img

Como mostrado na figura à esquerda, as variáveis globais a e b existem no arquivo de scripts Python.
As variáveis a e b dentro da função print_sum referem-se a um novo objeto separado, não ao objeto referenciado pela variável global.
Palavra-chave global
Aprenda como se referir a variáveis globais usando a palavra-chave global.
def print_sum():
	global a, b # a e b usam a e b declarados fora da função  # as variáveis globais a e b referem-se a 10 e 20
	a = 100 # As variáveis globais a e b referen-se a 100 e 200
	b = 200
    result = a + b
    print('print_sum() da função: a soma de ', a, ' e ', b, 'é: ',result)
a = 10 # Criar variáveis a e b referenciando a 10, 20
b = 20
print_sum()
result = a + b
print('print_sum() fora da função: a soma de ', a, ' e ', b, 'é: ',result)
Resultado:

print_sum() da função : a soma de 100 e 200 é 300

print_sum() fora da função: a soma de 100 e 200 é 300

Palavra-chave global

 Cuidado com o SintaxeError

def print_sum():
	global a = 0


Nota: global a = 100 causa um erro de sintaxe. A declaração global e o operador de cessão não podem ser usados ao mesmo tempo.

Processo global de referência variável

O processo de utilização das variáveis globais a e b em uma função através de uma declaração global explícita é o seguinte:
4.4. Global variable reference process img

Se você alterar o valor de uma variável declarada como global a ou b, o valor também é alterado fora da função.
Notas sobre o uso de constantes globais em variáveis globais

 Variáveis Globais vs. Constantes Globais

O uso de variáveis globais é uma prática muito ruim em todas as linguagens de programação, não apenas em Python. Quando o comprimento do código se torna longo, as variáveis globais tornam-se a principal causa de erros.
Por outro lado, as constantes globais não são necessariamente ruins.
Uma constante global é declarada com a palavra-chave global da seguinte forma. Ela pode ser declarada fora de uma função e referenciada em todo o módulo. Os valores das constantes globais estão geralmente em maiúsculas.
Uma constante é um número que não muda.
GLOBAL_VALUE = 1024 # Capitalizar constantes globais as torna mais fáceis de distinguir

def foo():
	global GLOBAL_VALUE
 a = GLOBAL_VALUE * 100
 print(a)
foo()
Resultado: 102400

Funções e métodos
Diferença entre a função e o método

As funções e métodos são equivalentes na medida em que executam uma ação definida para realizar uma tarefa específica. Entretanto, há uma diferença entre os dois.
Função - Um módulo na programação que recebe parâmetros (opcional) quando chamado, realiza uma operação específica, e retorna o resultado se necessário.
Método - Uma função ligada a um objeto tratado na programação orientada ao objeto.
Um método pode chamar objetos com valores diferentes, chamados de instâncias.
Isto será coberto em classe mais tarde.
Método format

Aprenda como fazer saída formatada ao exibir uma string. A saída formatada pode ser produzida chamando o método de string format.
Alojamento: Chaves {} em uma string é usado para produzir um argumento são chamados de placeholder.
Se você colocar um argumento no método .format() da seguinte forma, este valor do argumento aparece no espaço 
'{} Python!'.format('Hello') # Hello vai para o lugar das chaves
Resultado: 'Hello Python!'

'{} Python!'.format('Hi')
Resultado: 'Hi Python!'

'{0} Python!'.format('Hello') # {0} Python é chamado de string base ou string modelo
Resultado: 'Hello Python!'

Método format

Você pode controlar a ordem de saída atribuindo o valor inteiro (índice) requerido dentro do espaço reservado. (Por padrão, 0, 1, ... são atribuídos). 
'Eu gosto de {} e {}!'.format('Python', 'Java')
Resultado: 'Eu gosto de Python e Java!'

'Eu gosto de {0} e {1}!'.format('Python', 'Java') # Você pode colocar no lugar titulares de índice com 0, 1, ... etc. Dependendo do índice, Python ou Java é inserido, respectivamente.
Resultado: 'Eu gosto de Python e Java!'

'Eu gosto de {1} e {0}!'.format('Python', 'Java')
Resultado: 'Eu gosto de Java e Python!'



Método format

Você pode fazer várias saídas usando o número do espaço reservado, tais como {0}, {1}, {2}.
Um placeholder pode não ser apenas uma string, mas também um tipo de dado arbitrário, como um inteiro, como 100 ou 200, ou um número real.
Vamos dar uma olhada nos diferentes métodos de saída.
'{0}, {0}, {0}! Python'.format('Hello')
Resultado: 'Hello, Hello, Hello! Python'

'{0}, {0}, {0}! Python'.format('Hello', 'Hi')
Resultado: 'Hello, Hello, Hello! Python'

'{0} {1}, {0} {1}, {0} {1}! Python'.format('Hello', 'Hi')
Resultado: 'Hello Hi, Hello Hi, Hello Hi! Python'

'{0} {1}, {0} {1}, {0} {1}!'.format(100, 200)
Resultado: '100 200, 100 200, 100 200!'

Método format

No format, você pode colocar não apenas os valores literais das strings (valores fixos como inteiros, strings e tipos de dados booleanos), mas também variáveis ou objetos como se segue.
greet = "Olá'
'{} Mundo!'.format(greet)
Resultado: 'Olá Mundo!'

name = 'Davi'
print('Meu nome é {}!'.format(name))
Resultado: 'Meu nome é Davi!'

Linha 1, 2

Digite a sequência 'Davi' no nome.
Se você digitar um nome usando o método format, o valor do nome é digitado em {} (espaço reservado).
Método format

Este é um código de exemplo que toma o nome do usuário, a idade e o cargo como entradas, armazena-os em variáveis chamadas nome, idade e cargo, e os produz utilizando o método format.
name = input('Digite seu nome: ')
age = input('Digite sua idade: ')
job = input('Digite seu trabalho: ')

print('Seu nome é {}, sua idade é {} anos e seu trabalho é {}.'.format(name, age, job))
Resultado:

Digite seu nome: Davi

Digite sua idade: 23

Digite seu trabalho: Programador

Seu nome é Davi, sua idade é 23 anos e seu trabalho é Programador

O significado de {} dentro da função print significa imprimir o valor do argumento da função format onde {} está presente.
Usando o método format de uma string, o nome, idade e cargo são impressos nos campos {}, respectivamente.
Se o método format não for utilizado como acima, a declaração impressa aparece de forma complexa. Neste caso, há muitas vírgulas e aspas, o que torna o código difícil de ler e causa erros.
Conjunto de produtos

O conceito de um conjunto de produtos

Aprenda um conjunto de produtos, o tópico avançado de conjuntos discutido na seção anterior.
Vamos ver como criar facilmente um conjunto de produtos usando uma função.
O conjunto de produtos A3, um conceito utilizado em matemática, pode ser definido como A x A x A.
A x A x A tem os seguintes elementos.
A x A x A = (A x A) x A = {(1, 1)(1, 3),(3, 1),(3, 3)} x {(1, 3)}
          = {((1, 1), 1), ((1, 1), 3), ((1, 3), 1), ((1, 3), 3), ((3, 1), 1), ((3, 1), 3), ((3, 3), 1), ((3, 3), 3)} 
A operação acima pode ser implementada através da repetição da função product_set.
O conceito de um conjunto de produtos

Encontre o conjunto de produtos usando uma função.
Rever mais uma vez o conjunto de produtos discutidos no conceito chave da unidade anterior.
def product_set(set1, set2):
    res = set()
    for i in set1:
        for j in set2:
            res = res | {(i, j)} #product_set usa um duplo for loop
    return res
def exp(input_set, exponent): # Uma função que eleva input_set a
potência exponent
    res = input_set # reinicia
    for _ in range(exponent - 1):
        res = product_set(res, input_set)
    return res
A = {1, 3}
A3 = exp(A, 3) # Executa A a potencia 3
print(A3)
Resultado: {((3, 1), 3), ((3, 3), 1), ((3, 1), 1), ((1, 3), 3) ((1, 1), 1) ((3, 3), 3), ((1, 1), 3) ((1, 3),1)}

Linha 15

Quando um argumento é passado na função exp, exp chama o product_set para realizar um conjunto de multiplicação. Ou seja, a terceira potência é executada.
O número de todos os resultados possíveis quando um molde é enrolado duas vezes

Use a função product_set para contar o número de casos em que um dado é lançado duas vezes.
def product_set(set1, set2):
    res = set()
    for i in set1:
        for j in set2:
            res = res | {(i, j)} #product_set usa um duplo for loop
    return res
cases = { 1, 2, 3, 4, 5, 6 }
cases_2times = product_set(cases, cases)
print(cases_2times)
Resultado:

{(3, 4), (4, 3), (3, 1), (5, 4), (4, 6), (5, 1), (2, 2), (1, 6), (2, 5), (1, 3), (6, 2), (6, 5), (4, 2), (4, 5), (3, 3), (5, 6), (3, 6), (5, 3), (2, 4), (1, 2), (2, 1), (1, 5), (6, 1), (6, 4), (3, 2), (4, 1), (3, 5), (5, 2), (4, 4), (5, 5), (1, 1), (1, 4), (2, 3), (2, 6), (6, 6), (6, 3)}

Linha 8, 9

A variável de casos é atribuída como um tipo de conjunto de 1 a 6.
Multiplicar os dois casos. Em seguida, a combinação de dois números é atribuída como um tipo de conjunto. Todos os casos são devolvidos sem duplicatas.
"""