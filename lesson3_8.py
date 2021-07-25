matrix_n = []
n = 4
for i in range(n):
    matrix_n.append([])
    sum_num = 0
    for j in range(n):
        user_num = int(input(f'Введите элемент {i+1} строки и {j+1} столбца: '))
        sum_num += user_num
        matrix_n[i].append(user_num)

    matrix_n[i].append(sum_num)

for i in matrix_n:
    print(('{:>4d}' * 5).format(*i))
