s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60, 70}

print(s1 | s2)
print(f"=-="*10)

print(s1 & s2)
print(f"=-="*10)

print(s1 - s2)
print(f"=-="*10)

print(s1 ^ s2)
print(f"=-="*10)

print(s1.issubset(s2))
print(f"=-="*10)

print(s1.issuperset(s2))
print(f"=-="*10)

print(s1.isdisjoint(s2))
print(f"=-="*10)