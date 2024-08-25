"""
Поле в игре в одномерный морской бой имеет размеры 1 × n. Ваша задача — найти такое максимальное k,
что на поле можно расставить один корабль размера 1 × k , два корабля размера 1 × ( k − 1 ) , … , k
кораблей размера 1 × 1, причем корабли, как и в обычном морском бое, не должны касаться друг друга и пересекаться.

Выведите единственное число — такое максимальное k, что можно расставить корабли, как описано в условии.

|-----------------------|
|--- time limit: 2 s ---|
|- memory limit: 256 Mb |
|-----------------------|

"""


def ship_space(k):
    return k * (k ** 2 + 3 * k + 2) // 6


def empty_cells(k):
    return k * (k + 1) // 2 - 1


def find_max_k(n):
    left, right = 0, n
    while left < right:
        mid = (left + right + 1) // 2
        # if ship_space(mid) + empty_cells(mid) <= n:
        if (mid ** 3 + 6 * mid * mid + 5 * mid) // 6 - 1 <= n:
            left = mid
        else:
            right = mid - 1
    return left


n = int(input())
max_k = find_max_k(n)
print(max_k)
