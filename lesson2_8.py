st, num = map(str, input('Введите натуральное число и искомую цифру->').split())
col_num = 0
for i in st:
    if i == num:
        col_num += 1

print(f'В числе {st} количество вхождений цифры {num} = {col_num}')
