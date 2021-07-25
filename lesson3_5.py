import random

n = 100
r = [random.randint(-100, 100) for _ in range(n)]
print(f'Массив: {r}')

min_i = 0

for i in r:
    if r[min_i] > i:
        min_i = r.index(i)

if r[min_i] >= 0:
    print(f'В массиве нет отрицательных элементов')
else:
    print(f'В массиве минимальный отрицательный элемент: {r[min_i]}. Находится в массиве на позиции {min_i}')
