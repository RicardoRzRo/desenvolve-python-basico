import random

l = []
for i in range(20):
    l.append(random.randint(-100, 100))
print(sorted(l))
print(l)
print(l.index(max(l)))
print(l.index(min(l)))