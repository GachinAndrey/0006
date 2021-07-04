""" 1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python и разрядность
вашей ОС.
"""

import sys


def show_size(x, level=0):
    size_par = sys.getsizeof(x)
    print('\t' * level, f'type={type(x)}, size={size_par}, object={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                size_par = size_par + sys.getsizeof(key)
                show_size(value, level + 1)
                size_par = size_par + sys.getsizeof(value)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)
                size_par = size_par + sys.getsizeof(item)
    return size_par


number = input('Введите число: ')

sum_ = 0
prod = 1

for f in number:
    sum_ += int(f)
    prod *= int(f)
print(f"Сумма цифр числа {number}: {sum_}")
print(f"Произведение цифр: {number}: {prod}")

sum_member = sys.getsizeof(number) + sys.getsizeof(sum_) + sys.getsizeof(prod)
print('В программе задействовано байт памяти: {}'.format(sum_member))

