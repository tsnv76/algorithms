
a, b, c = map(int, input("Введите три разных целых числа числа: a, b и c -> ").split())

# Первое решение
if a > b:
    if a < c:
        print(f'Среднее число -> {a = }')
    elif b > c:
        print(f'Среднее число -> {b = }')
else:
    if b < c:
        print(f'Среднее число -> {b = }')
    elif a > c:
        print(f'Среднее число -> {a = }')
    else:
        print(f'Среднее число -> {c = }')

# Второе решение
if b < a < c or c < a < b:
    print(f'Среднее число -> {a = }')
elif a < b < c or c < b < a:
    print(f'Среднее число -> {b = }')
else:
    print(f'Среднее число -> {c = }')
