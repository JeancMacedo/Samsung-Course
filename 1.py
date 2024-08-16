list_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list_array,'\n')
list_array = [[1, 2, 3],
			  [4, 5, 6],
              [7, 8, 9]]
print(list_array,'\n')

list_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list_array[0],'\n')

#se quiser entender visualmente acesse o capitulo 13, 
#ta completinho lá

list_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i,j,k in list_array:
	print(i,j,k)
print('\n')
list_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in list_array:
 for j in i:
  print(j, end = ' ')
 print()
print('\n')

list_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(list_array)):
    for j in range(len(list_array[i])):
        print(list_array[i][j], end = ' ')
    print()
print('\n')

list_array = [[1, 2, 3], [4, 5], [7]]
for i in range(len(list_array)):
    for j in range(len(list_array[i])):
        print(list_array[i][j], end = '')
    print()
print('\n')

import copy
list_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list1 = copy.deepcopy(list_array)
list1[0][0] = 90
print(list_array)
print (list_array is list1)
print('\n')

list1 = []
for i in range(3):
    line = []
    for j in range(2):
        line.append(0)
    list1.append(line)
print(list1)
print('\n')

list1 = [1, 2, 3, 4, 5]
list2 = []

for i in list1:
    line = []
    for j in range(i):
        line.append(j)
        list2.append(line)

print(list2)
print('\n')

listl = [1, 2, 3, 4, 5]
list2 = []
for i in listl:
    line = []
    for j in range(i):
        line.append(j)
        print(j,  end = ' ')
    list2.append(line)
    print()
print('\n')

import random
list1 = [1, 2, 3, 4, 5]
list2 = []
for i in listl:   
    line = []
    for j in range(i) :
        line.append(random.randint(1, 100)) #preza valores aleatórios
    list2.append(line)
for i in list2:
    for j in i:
        print(j, end = ' ')
    print()