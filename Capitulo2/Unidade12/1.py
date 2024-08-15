pop_a = (100,150,230,120,180,100,140,95,81,21,4)
pop_b=(300,420,530,420,400,300,40,5,1,1,1)
old_a = sum(pop_a[7:])
print(old_a)
old_b = sum(pop_b[7:])
print(old_b)
sumA, sumB = sum(pop_a), sum(pop_b)
print(sumA)
print(sumB)
oldRateA, oldRateB = old_a/sumA, old_b/sumB
print('Os graus de envelhecimento nas cidades A e B são {:5.3f} e {:5.3f}, respectivamente.'.format(oldRateA, oldRateB))
#Os graus de envelhecimento nas cidades A e B são 0,165 e 0,003, respectivamente.
