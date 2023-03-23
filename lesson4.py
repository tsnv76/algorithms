'''1-2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
Проанализировать скорость и сложность этих алгоритмов
Решение двух задач в одной программе
'''


import math
import timeit


def func_without_eratosfen(n):
    #Функция поиска i-го простого числа, без использования алгоритма «Решето Эратосфена»

    lst_prime = [2]
    number = 3
    while len(lst_prime) < n:
        flag = True
        for j in lst_prime.copy():
            if number % j == 0:
                flag = False
                break
        if flag:
            lst_prime.append(number)
        number += 1
    return lst_prime[-1]


def func_with_eratosfen(i):
    #Функция поиска i-го простого числа, используя алгоритм «Решето Эратосфена»

    i_max = prime_counting_function(i)
    lst_prime = [_ for _ in range(2, i_max)]

    for number in lst_prime:
        if lst_prime.index(number) <= number - 1:
            for j in range(2, len(lst_prime)):
                if number * j in lst_prime[number:]:
                    lst_prime.remove(number * j)
        else:
            break
    return lst_prime[i - 1]


def prime_counting_function(i):
    '''Функция возвращает верхнюю границу отрезка на котором лежат
    i-e количество простых чисел. Функция основана на теореме о
    распределении простых чисел: количество простых чисел на отрезке
    [1;n] растёт с увеличением n как n / ln(n).
    '''

    number_of_primes = 0
    number = 2
    while number_of_primes <= i:
        number_of_primes = number / math.log(number)
        number += 1
    return number


user_number = int(input('Введите номер по счету простого числа: '))
print('*' * 50)
num_exec = 1
test_times = 1000

print('Алгоритм без использования алгоритма «Решето Эратосфена»')
print(f'{user_number} по счёту простое число - {func_without_eratosfen(user_number)} ')
time1 = timeit.timeit(f'func_without_eratosfen({test_times})',
                      setup='from __main__ import func_without_eratosfen',
                      number=num_exec)
print(f'Время исполнения алгоритма-> {time1}')
print('*' * 50)
print('Алгоритм с использованием алгоритма «Решето Эратосфена»')
print(f'{user_number} по счёту простое число - {func_with_eratosfen(user_number)}')
time2 = timeit.timeit(f'func_with_eratosfen({test_times})',
                      setup='from __main__ import func_with_eratosfen',
                      number=num_exec)
print(f'Время исполнения алгоритма-> {time2}')
print('*' * 50)
print(f'Программа без использования алгоритма «Решето Эратосфена» быстрее \
программы с использованием алгоритма «Решето Эратосфена» в {round(time2 / time1, 2)} раз')
