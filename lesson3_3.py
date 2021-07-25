import random

n = 10
r = [random.randint(1, 100) for _ in range(n)]
print(f'Массив до изменения: {r}')

max_r = r[0]
min_r = r[0]

for i in r:
    if i > max_r:
        max_r = i
    elif i < min_r:
        min_r = i
min_i = r.index(min_r)
max_i = r.index(max_r)
r[min_i], r[max_i] = r[max_i], r[min_i]
print(f'Поменяли местами элементы с индексами [{min_i}] и [{max_i}]: {r}')
