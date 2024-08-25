str1 = ['a', 'b', 'c', 'b', 'a', 'b', 'c']
dic = {}
for ch in str1:
   if ch not in dic.keys():
     dic[ch] = 0
   dic[ch] +=1
print ('alphabet counting :', dic)
print(f'-=' * 30)
str1 = ['a', 'b', 'c', 'b', 'a', 'b', 'c']
dic = {}
for ch in str1:
   dic.setdefault(ch, 0)
   dic[ch] += 1
   print(list(dic.items()))

print('alphabet counting :', dic)
print(f'-=' * 30)
dic = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
dic.setdefault('f', 50)
print(dic)
print(f'-=' * 30)
dic = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
dic.update(a = 90)
print(dic)
dic.update(e = 50)
print(dic)
print(f'-=' * 30)
dic2 = {1: 'um', 2: 'dois'}
dic2.update({1: 'UM', 3: 'TRÊS'})
print(dic2)
print(f'-=' * 30)
dic = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print (dic.pop('a'))
print(dic)
print(f'-=' * 30)
dic = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(dic.popitem())
print(dic)
#popitem apaga qualquer par de valor chave e devolve o par.
print(f'-=' * 30)
dic = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(dic)
dic.clear()
print (dic)
print(f'-=' * 30)
dic = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
a = dic.get('a')
print (a)
print(f'-=' * 30)
dic = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(dic.keys())
print(f'-=' * 30)
for str1, num in dic.items():
   print(str1, ':', num)

"""
Método               Função



keys()	      Devolve todas as chaves do dicionário.
values()	    Devolve todos os valores do dicionário.
items()     	Devolve todos os itens do dicionário em pares [chave]:[valor].
get(key)	    Retorna o valor da chave. Se não houver chave, devolve Nenhuma.
pop(chave)	  Devolve o valor da chave e apaga o item. Se não houver chave, causa uma exceção KeyError.
popitem()	    Devolve o item selecionado aleatoriamente e apaga o item.
clear()     	Excluir todos os itens do dicionário.
"""