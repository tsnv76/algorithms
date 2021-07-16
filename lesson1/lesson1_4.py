from os import urandom as _urandom

def rand_s(list): #Функция возвращает случайный элемент из списка.
    rand_num = int(int.from_bytes(_urandom(10), 'big'))
    len_list = len(list)
    i = rand_num % len_list
    return list[i]


def frange(start, stop, step): #Функция генерирует диапазон вещественных чисел
    while start < stop:
        yield start
        start += step


print('Введите диапазон. Диапазон целых чисел (type_range = int start end step). \
Или диапазон вещественных чисел (type_range = float start end step). \
Или диапазон символов (type_range = str start end step) ')

type_range, raw_start, raw_end, raw_step = map(str, input('Введите диапазон: type_range start end step: ').split())

if type_range == 'int':
    start = int(raw_start)
    stop = int(raw_end)
    step = int(raw_step)
    list_int = [num for num in range(start, stop + 1, step)]
    print(f'Случайное целое число из диапазона {start} - {stop}: {rand_s(list_int)}')

elif type_range == 'float':
    start = float(raw_start)
    stop = float(raw_end)
    step = float(raw_step)
    list_float = [x for x in frange(start, stop + step, step)]
    print(f'Случайное вещественное число из диапазона {start} - {stop}: {rand_s(list_float)}')

elif type_range == 'str':
    start = raw_start
    stop = raw_end
    step = int(raw_step)
    list_str = [chr(i) for i in range(ord(start), ord(stop) + 1, step)]
    print(f'Случайный символ из из диапазона {start} - {stop}: {rand_s(list_str)}')

else:
    print('Неправильно задан диапазон')