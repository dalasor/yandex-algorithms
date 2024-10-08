"""
Задано две строки, нужно проверить, является ли одна анаграммой другой. Анаграммой называется строка, полученная из другой перестановкой букв.

Формат ввода
Строки состоят из строчных латинских букв, их длина не превосходит 100000. Каждая записана в отдельной строке.

Формат вывода
Выведите "YES" если одна из строк является анаграммой другой и "NO" в противном случае.

|-----------------------|
|--- time limit: 1 s ---|
|- memory limit: 64 Mb-|
|-----------------------|

"""


def h(s: str) -> int:
    char_count = [0] * 26
    for char in s:
        char_count[ord(char) - ord('a')] += 1

    # Полиномиальное хэширование
    hash_value = 0
    p = 31  # Простое число, основание для хэширования
    p_pow = 1
    mod = 10**9 + 9  # Большое простое число для модуля

    for i in range(26):
        hash_value = (hash_value + (char_count[i] + 1) * p_pow) % mod
        p_pow = (p_pow * p) % mod

    return hash_value


print(('NO', 'YES')[h(input()) == h(input())])
