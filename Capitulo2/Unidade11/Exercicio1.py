frutas_dic = {'maçã': 6000,'melão': 3000,'banana': 5000,"laranja": 4000}
print(frutas_dic)
dict_keys = (['maçã', 'melão', 'banana', 'laranja'])
print('\n',dict_keys)
if 'maçã' in frutas_dic:
    print(f'\nmaçã pertence a {frutas_dic}')
if 'manga' not in frutas_dic:
    print(f'\nmanga não pertence a {frutas_dic}')