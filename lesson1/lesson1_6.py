num_letter = int(input('Введите номер буквы в алфавите: '))

# Генерация списка букв
list_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
print(list_letters)
if num_letter <= len(list_letters):
    print(f'Буква под номером {num_letter}: {list_letters[num_letter - 1]}')
else:
    print(
      f'Введено число превышающее количество букв в алфавите ({len(list_letters)})'
    )