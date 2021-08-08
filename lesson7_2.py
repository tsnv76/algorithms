# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
import random


def merge_sort(arr):

    def merge(first, second):
        res = []
        i, j = 0, 0

        while i < len(first) and j < len(second):

            if first[i] < second[j]:
                res.append(first[i])
                i += 1

            else:
                res.append(second[j])
                j += 1

        res.extend(first[i:] if i < len(first) else second[j:])
        return res

    def div_half(lst):
        if len(lst) == 1:
            return lst

        elif len(lst) == 2:
            return lst if lst[0] <= lst[1] else lst[::-1]

        else:
            return merge(div_half(lst[:len(lst)//2]), div_half(lst[len(lst)//2:]))
    return div_half(arr)


array_size = 10
min_ = 0
max_ = 50
array = [random.uniform(min_, max_) for _ in range(array_size)]

print('Несортированный массив:', array, sep='\n')
print(f'Массив после сортировки:', merge_sort(array), sep='\n')
