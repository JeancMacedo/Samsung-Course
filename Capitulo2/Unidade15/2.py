phone_book = {"David Doe": "010-1234-5678", "John Smith": "010-1234-5679", "Jane Carter": "010-1234-5680"}
print(phone_book.items())
print(f'-='*30)
print(phone_book.keys())
print(f'-='*30)
print(phone_book.values())
print(f'-='*30)
for name, phone_num in phone_book.items():
  print(name, ':', phone_num)
print(f'-='*30)
'''
  O que é um módulo?

Módulo
É um arquivo Python com funções, variáveis ou classes.
O Python tem muitos módulos desenvolvidos por inúmeros desenvolvedores.
Ao importar um módulo existente, escreva o nome do módulo após import.
Ao importar dessa maneira, use um ponto (.) após nome do módulo, como mostrado abaixo, para acessar seus componentes
import [nome do módulo].[nome da classe].[ nome do método].

A palavra-chave que traz o módulo é import. 
import nome_do_modulo_1[, nome_do_modulo_2, ...]
'''
import datetime
print(datetime.datetime.now())
print(f'-='*30)

today = datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(f'-='*30)

print(dir(datetime))
print(f'-='*30)

import datetime as dt #usar dt em vez de datetime a partir de agora
start_time = dt.datetime.now()
print(start_time.replace(month=12, day=25))
print(f'-='*30)

import time
seconds = time.time()
print('Tempo depois de epoch =', seconds)

import time
unix_timestamp = time.time()
local_time = time.localtime(unix_timestamp)
print(time.strftime('%Y-%m-%d %H:%M:%S', local_time))
print(f'-='*30)

#Vamos descobrir as funções  do módulo usando-as
import math as m
print(m.pow(3, 3)) #3 elevado à potência 3
print(m.fabs(-99)) #O valor absoluto de -99
print(m.ceil(2.1)) #2.1 arredondado para cima
print(m.ceil(-2.1)) #-2.1 arredondado para cima
print(m.floor(2.1)) #-2.1 arredondado para baixo
print(m.log(2.71828))

print(f'-='*30)
"""
Funções matemáticas no módulo de math, descrição e exemplos de uso
Função	Descrição	Exemplo
fabs(x)	Devolve o valor absoluto do número real x	fabs(-2) → 2.0
ceil(x)	
Arredonda x para o maior inteiro mais próximo

ceil(2.1) → 3, ceil(-2.1) → -2
floor(x)	Arredonda x para o menor inteiro mais próximo	floor(2.1) → 2, floor(-2.1) → -3
exp(x)	Retorna e^x.	exp(1) → 2.71828
log(x)	Devolve o logaritmo natural x.	log(2.71828) → 1.0
log(x, base)	Retorna o valor do log x na base "base".	log(100, 10) → 2.0
sqrt(x)	Devolve a raiz quadrada de x.	sqrt(4.0) → 2.0 
sin(x)	Retorna o valor seno de x em radianos.	sin(3.14159/2) → 1, sin(3.14159) → 0
asin(x)	Devolve asin de x.	asin(1.0) → 1.57, asin(0.5) → 0.523599
cos(x)	Devolve o valor de cosseno de x em radianos.	cos(3.14159/2) → 0, cos(3.14159) → -1
acos(x)	Devolve acos de x.	acos(1.0) → 0, acos(0.5) → 1.0472
tan(x)	Retorna o valor da tangente de x em radianos.	tan(3.14159/4) → 1, tan(0.0) → 0
degrees(x)	Muda o ângulo x de radianos para graus.	degrees(1.57) → 90
radians(x)	Muda o ângulo em graus x para radianos.	radians(90) → 1.57


Funções trigonométricas utilizando radianos

Vamos descobrir por que o sin(90) não é 1 no código abaixo.
Isto porque a função trigonométrica no módulo math do Python usa ângulos em radianos como parâmetros.
Para utilizar o ângulo como 90 graus, é necessário convertê-lo para uma notação radiana, como math.pi/2.0.
"""
import math as m

print(m.sin(0.0)) #valor do seno ângulo 0
print(m.sin(90.0)) #não usar ângulo em graus como 90,0
print(m.sin(m.pi/2)) #notação radiana