n = int(input('Введите количество элементов: '))
x = 1
sum_num = 0
for i in range(n):
    sum_num += x
    x /= -2

print(f'Сумма {sum_num}')
