
x1, y1, x2, y2 = map(int, input('Введите кординаты (x1 y1 x2 y2): ').split())

k = (y2 - y1)/(x2 - x1)
b = y1 - k * x1

print(f'Уравнение прямой: y = {k}x + {b}')