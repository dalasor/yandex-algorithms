"""
Дан массив из N целых чисел. Все числа от − 10^9 до 10^9. Нужно уметь отвечать на запросы вида
“Cколько чисел имеют значения от L до R ?”.

Формат ввода
Число N ( 1 ≤ N ≤ 10^5 ). Далее N целых чисел.
Затем число запросов K (1 ≤ K ≤ 10^5). Далее K пар чисел L, R (−10^9 ≤ L ≤ R ≤ 10^9 ) — собственно запросы.

Формат вывода
Выведите K чисел — ответы на запросы.

|-----------------------|
|--- time limit: 3 s ---|
|- memory limit: 64 Mb -|
|-----------------------|

"""


def lrbinsearch(n, arr, target, isl: bool):
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if isl:
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        else:
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid
    return left


n = int(input())
nums = sorted([int(i) for i in input().split()])
k = int(input())
results = []

for i in range(k):
    l, r = map(int, input().split())
    l_ind = lrbinsearch(n, nums, l, True)
    r_ind = lrbinsearch(n, nums, r, False)
    results.append(r_ind - l_ind)

print(*results)

