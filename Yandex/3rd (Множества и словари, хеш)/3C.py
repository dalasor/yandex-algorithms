"""
Дан массив a из n чисел. Найдите минимальное количество чисел, после удаления которых попарная
разность оставшихся чисел по модулю не будет превышать 1, то есть после удаления ни одно число
не должно отличаться от какого-либо другого более чем на 1.

|-----------------------|
|--- time limit: 1 s ---|
|- memory limit: 256 Mb-|
|-----------------------|

"""


# Методом скользящего окна
def min_removal_count_window(a: list) -> int:
    a.sort()
    max_set_size = 1
    i = 0

    for j in range(n):
        while i < n and a[j] - a[i] > 1:
            i += 1
        max_set_size = max(max_set_size, j - i + 1)

    return n - max_set_size


# С помощью словаря
def min_removal_count_dict(a: list) -> int:
    count = {}
    for num in a:
        count[num] = count.get(num, 0) + 1

    max_valid_count = 0
    for num in count:
        max_valid_count = max(max_valid_count, count[num] + count.get(num + 1, 0))

    return len(a) - max_valid_count


n = int(input())
nums = list(map(int, input().split()))

print(min_removal_count_window(nums))
print(min_removal_count_dict(nums))
