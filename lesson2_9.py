def sum_num(n):
    s = 0
    for f in n:
        s += int(f)
    return s


list_number = list(map(str, input('Введите числа и нажмите Enter').split()))

max_number = 0
max_sum = 0
for i in list_number:
    s_n = sum_num(i)
    if s_n > max_sum:
        max_number = i
        max_sum = s_n

print(f'У числа {max_number} была наибольшая сумма цифр - {max_sum}')
