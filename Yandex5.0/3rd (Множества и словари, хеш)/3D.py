"""
Вам дана последовательность измерений некоторой величины. Требуется определить, повторялась ли какое-либо число,
причём расстояние между повторами не превосходило k.

Формат ввода
В первой строке задаются два числа n и k (1 ≤ n, k ≤ 10^5).
Во второй строке задаются n чисел, по модулю не превосходящих 10^9.

Формат вывода
Выведите YES, если найдется повторяющееся число и расстояние между повторами не превосходит k и NO в противном случае.

|-----------------------|
|--- time limit: 1 s ---|
|- memory limit: 64 Mb -|
|-----------------------|
"""


def is_repeat(n, k, nums) -> str:
    counts = {}
    for i in range(n):
        if nums[i] in counts:
            if i - counts[nums[i]] <= k:
                return 'YES'
            else:
                counts[nums[i]] = i
        else:
            counts[nums[i]] = counts.get(nums[i], i)
    return 'NO'


n, k = map(int, input().split())
nums = list(map(int, input().split()))
print(is_repeat(n, k, nums))
