import random

n = 100
r = [random.randint(1, 100) for _ in range(n)]
print(f'Массив: {r}')

min_i_1 = 0
min_i_2 = 1

for i in r:
    if r[min_i_1] > i:
        min_i_2 = min_i_1
        min_i_1 = r.index(i)
    elif r[min_i_2] > i:
        min_i_2 = r.index(i)

print(f'Два наименьших элемента: {r[min_i_1]} и {r[min_i_2]}')

#Второй способ через сортировку списка

sort_list = []
sort_list.extend(r)
sort_list.sort()

print(f'Два наименьших элемента (второй способ): {sort_list[0]} и {sort_list[1]}')
