import random

matr_n = []
n = 10

for i in range(n):
    matr_n.append([])
    matr_n[i].extend([random.randint(1, 100) for _ in range(n)])

min_list = []
min_list.extend(matr_n[0])

for num in matr_n:
    print()
    print(('{:4d} ' * len(num)).format(*num))
    i = 0
    for j in num:
        if j < min_list[i]:
            min_list[i] = j
        i += 1

print()
print('Массив из минимальных элементов столбцов матрицы ')
print(('{:4d} ' * len(min_list)).format(*min_list))
print()

min_list.sort(reverse=True)
print('Максимальный элемент среди минимальных элементов столбцов матрицы: ', min_list[0])
