""" Нумерация дробей """

"""
Георг Кантор доказал, что множество всех рациональных чисел счетно 
(т.е. все рациональные числа можно пронумеровать).

Чтобы упорядочить дроби необходимо их положить в таблицу, как показано на рисунке.
В строку с номером i этой матрицы по порядку записаны дроби с числителем i, 
а в столбец с номером j дроби с знаменателем j.

Вам требуется по числу n найти числитель и знаменатель n-ой дроби.
В выходной файл требуется вывести через символ / два числа: числитель и знаменатель соответствующей дроби.

|-----------------------|
|--- time limit: 2 s ---|
|- memory limit: 256 Mb-|
|-----------------------|

"""


def calculate_height(k):
    # Возвращает количество элементов в первых k диагоналях
    return k * (k + 1) // 2


def find_fraction(n):
    # Бинарный поиск для определения, в какой диагонали находится n-ая дробь
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if calculate_height(mid) < n:
            left = mid + 1
        else:
            right = mid

    diagonal = left
    # Количество элементов до найденной диагонали
    total_before = calculate_height(diagonal - 1)
    # Позиция в диагонали
    position = n - total_before

    # Определяем числитель и знаменатель для n-ой дроби
    if diagonal % 2 == 0:
        # Для нечетной диагонали
        numerator = diagonal - position + 1
        denominator = position
    else:
        # Для четной диагонали
        numerator = position
        denominator = diagonal - position + 1

    return numerator, denominator


n = int(input())
numerator, denominator= find_fraction(n)
print(f"{numerator}/{denominator}")
