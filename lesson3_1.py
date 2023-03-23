result = {}
for i in range(2, 10):
    result[i] = []
    for f in range(2, 100):
        if f % i == 0:
            result[i].append(f)
    print(f'Для числа {i} кратны - {len(result[i])}. Кратные числа: {result[i]}.')
