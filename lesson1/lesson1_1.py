number = input('Введите целое трехзначное число число: ')

sum_num = 0
mul_num = 1

for num in number:
    sum_num += int(num)
    mul_num *= int(num)
print(f"Сумма цифр числа {number}: {sum_num}")
print(f"Произведение цифр: {number}: {mul_num}")
