S = 'Welcome to Python'
S.split()
print(S.split( ))

print(f'-=' * 30)

S = '2021.8.15'
print(S.split('.'))
S = 'Hello, World!'
print(S.split(','))

print(f'-=' * 30)

s =  'Welcome, to, Python, and, bla, bla '
[x.strip() for x in s.split(',')] 
print([x.strip() for x in s.split(',')] )
#apaga espaço antes e depois do caractere separador.

print(f'-=' * 30)

s = "     Hello, World!!    "
print(s.strip())
print(s.lstrip())
print(s.rstrip())

print(f'-=' * 30)

s = "########this is an example#####"
print(s.strip('#'))

print(f'-=' * 30)

s = "########this is an example#####"
print(s.lstrip('#'))
print(s.rstrip('#'))

print(f'-=' * 30)

print('-'.join('010.1234.5678'.split('.')) )
#mudar o número de telefone com . para -

print(f'-=' * 30)

print(''.join(['apple', 'grape', 'banana']))

print(f'-=' * 30)

s = 'hello world'
clist = list(s)
print(clist)

print(f'-=' * 30)

a_string = 'Actions \n\t speak louder than words'
print(a_string)

print(f'-=' * 30)

word_list = a_string.split()
refined_string = " ".join(word_list)
#mudança de linha e a separação por aspas desaparece de a_string
print(refined_string)

print(f'-=' * 30)

s = 'Hello, World!'
print(s.lower())
print(s.upper())

print(f'-=' * 30)

s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(s.startswith('A'))
print(s.startswith('B',1))
print(s.startswith('B',5))
print(s.endswith('Z'))
print(s.endswith('C', 1, 3))
print(s.endswith('C', 1, 10))

print(f'-=' * 30)

text = '123,456,789,999'
replaceAll= text.replace(",","")
replace_t1 = text.replace(",", "", 1)
replace_t2 = text.replace(",", "", 2)
replace_t3 = text.replace(",", "", 3)
print("Resultado :")
print(replaceAll)
print(replace_t1)
print(replace_t2)
print(replace_t3)