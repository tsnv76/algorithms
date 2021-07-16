letter1, letter2 = map(str, input('Введите две буквы (строчные), через пробел (a - z): ').split())

# Генерация списка букв
list_str = [chr(i) for i in range(ord('a'), ord('z') + 1)]

index_letter1 = list_str.index(letter1) + 1
index_letter2 = list_str.index(letter2) + 1

if index_letter1 < index_letter2:
    step = 1
else:
    step = -1

print(f'Первая буква {letter1}, находится на позиции: {index_letter1}')
print(f'Вторая буква {letter2}, находится на позиции: {index_letter2}')

print(f'Между ними находятся буквы   {list_str[list_str.index(letter1) + step:list_str.index(letter2):step]} \
    ({abs(index_letter1 - index_letter2) - 1})')
