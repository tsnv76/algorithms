s1 = input('Введите натуральное число->')
chet = 0
nechet = 0
for num in s1:
    if int(num) % 2 != 0:
        nechet +=1
    else:
        chet +=1

print(f'В чсиле {s1} -> Четных {chet}, нечетных {nechet}')
