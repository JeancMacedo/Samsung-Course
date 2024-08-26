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