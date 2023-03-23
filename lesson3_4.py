import random

n = 100
r = [random.randint(1, 100) for _ in range(n)]
print(f'Массив: {r}')

max_i = 0
for i in r:
    if r.count(max_i) < r.count(i):
        max_i = r.index(i)

print(f'Число {r[max_i]}, встречается {r.count(max_i)} раза')
