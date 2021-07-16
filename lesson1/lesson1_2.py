n1 = 5
n2 = 6
bit_or = n1 | n2  # "ИЛИ"

bit_xor = n1 ^ n2 #  Исключительное "ИЛИ"

bit_and = n1 & n2 #"И"

#  Побитовое отрицание
bit_not_n1 = ~n1
bit_not_n2 = ~n2

bit_shift_right = n1 >> 2  # Побитовый сдвиг вправо
bit_shift_left = n1 << 2  # Побитовый сдвиг влево.

print(f"""Побитовое «ИЛИ» (OR) для {bin(n1)} и {bin(n2)}: \
{bin(bit_or)} ({bit_or})""")

print(f"""Исключающее «ИЛИ» (XOR) для {bin(n1)} и {bin(n2)}: \
{bin(bit_xor)} ({bit_xor})""")

print(f"""Побитовое «И» (AND) для {bin(n1)} и {bin(n2)}: \
{bin(bit_and)} ({bit_and})""")

print(f"""Побитовое отрицание (NOT) для {bin(n1)}: \
{bin(bit_not_n1)} ({bit_not_n1}) и для {bin(n2)}: \
{bin(bit_not_n2)} ({bit_not_n2})""")

print(f"""Битовый сдвиг вправо для {bin(n1)}: \
{bin(bit_shift_right)} ({bit_shift_right})""")

print(f"""Битовый сдвиг влево для {bin(n1)}: \
{bin(bit_shift_left)} ({bit_shift_left})""")