import random

n = 10
r = [random.randint(1, 100) for _ in range(n)]
print(f'Первый массив {r}')
index_r = []

for n in r:
    if n % 2 == 0:
        index_r.append(r.index(n))

print(f'Индексы чётных элементов первого массива: {index_r}')

