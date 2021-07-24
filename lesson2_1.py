s1, s2, operand = map(str, input('Введите два числа и символ арифмитической операции: + - * или /:  ').split())

x1 = int(s1)
x2 = int(s2)

if operand == "+":
    print(f'{x1} {operand} {x2} = {x1 + x2}')
elif operand == "-":
    print(f'{x1} {operand} {x2} = {x1 - x2}')
elif operand == "*":
    print(f'{x1} {operand} {x2} = {x1 * x2}')
elif operand == "/" and x2 != 0:
    print(f'{x1} {operand} {x2} = {x1 / x2}')
else:
    print('Результата нет')
if x2 == 0:
    print(f'Делить на 0 нельзя!')
