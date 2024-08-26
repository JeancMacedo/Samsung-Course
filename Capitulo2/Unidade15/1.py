keys = ('a', 'b', 'c', 'd')
x = dict.fromkeys(keys)
print(x)
print(f'-='*30)

y = dict.fromkeys(keys, 100)
print(y)
print(f'-='*30)

from collections import defaultdict #trazer o defaultdict do módulo de collections
keys  = ('a', 'b', 'c', 'd')
y = dict.fromkeys(keys, 100)
y = defaultdict(int) #definir o valor padrão como int
print(y['z'])
'''Não há chave 'z' no dicionário y, 
mas se você buscar o valor da chave, como y['z'], 
você encontrará 0. 
Isto porque o valor padrão da função int() é 0.
'''
print(f'-='*30)

from collections import defaultdict
word = 'abcbaabca'
counter = defaultdict(int)
for letter in word:
  counter[letter] += 1
print(counter)
print(f'-='*30)

list_dict = defaultdict(list)
print(list_dict)
defaultdict(list, {})
print(list_dict['list1'])
print(f'-='*30)

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for i in x:
    print(i, end = ' ')
    continue
print()
print(f'-='*30)

'''for key, value in dictionary.items():
 Código a repetir
'''
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for key, value in x.items():
    print(key, value)
print(f'-='*30)

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for value in x.values():
    print(value,  end=' ')
print()

print(f'-='*30)
planeta_telurico = {    
    'Mercúrio': {
        'raio_medio': 2439.7,
        'massa': 3.3022E+23,
        'periodo_orbital': 87.969,
    },
    'Venus': {
        'raio_medio': 6051.8,
        'massa': 4.8676E+24,
        'periodo_orbital': 224.70069,
    },
    'Terra': {
        'raio_medio': 6371.0,
        'massa': 5.97219E+24,
        'periodo_orbital': 365.25641,
    },
    'Marte':  {
        'raio_medio': 3389.5,
        'massa': 6.4185E+23,
        'periodo_orbital': 686.9600,
    }
}
print(planeta_telurico['Venus']['raio_medio'])
print(f'-='*30)

x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
import copy #chamar módulo copy
y = copy.deepcopy(x) #cópia profunda usando a função deepcopy
y['a']['python'] = '2.7.15'
print(x)
print(y)
print(f'-='*30)



