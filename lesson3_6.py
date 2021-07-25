import random

n = 10
r = [random.randint(1, 100) for _ in range(n)]
print(f'Массив: {r}')

min_i = 0
max_i = 0
step = 1
sum_num = 0

for i in r:
    if r[min_i] > i:
        min_i = r.index(i)
    elif r[max_i] < i:
        max_i = r.index(i)

if max_i - min_i < 0:
    step = -1

for i in r[min_i + step:max_i:step]:
    sum_num += i

print(f'Сумма элементов между минимальным ({r[min_i]}) и максимальным ({r[max_i]}) элементами: {sum_num}')
