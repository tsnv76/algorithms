
x1 = input('Введите натуральное число->')
s = ''
x = int(x1)
for i in range(len(x1)):
    s = s + str(x % 10)
    x = x // 10

print(f'Было> {x1}. Стало> {s}')
