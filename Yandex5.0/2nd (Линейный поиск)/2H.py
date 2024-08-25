"""
Константин и Михаил играют в настольную игру «Ярость Эльфов». В игре есть n рас и m классов персонажей.
Каждый персонаж характеризуется своими расой и классом. Для каждой расы и каждого класса существует
ровно один персонаж такой расы и такого класса. Сила персонажа i-й расы и j-го класса равна ai j,
и обоим игрокам это прекрасно известно.

Сейчас Константин будет выбирать себе персонажа. Перед этим Михаил может запретить одну расу и один класс,
чтобы Константин не мог выбирать персонажей, у которых такая раса или такой класс. Конечно же, Михаил старается,
чтобы Константину достался как можно более слабый персонаж, а Константин, напротив, выбирает персонажа посильнее.
Какие расу и класс следует запретить Михаилу?

В единственной строке выведите два целых числа через пробел — номер расы и номер класса, которые следует
запретить Михаилу. Расы и классы нумеруются с единицы. Если есть несколько возможных ответов, выведите любой из них.

|-----------------------|
|--- time limit: 3 s ---|
|- memory limit: 256 Mb-|
|-----------------------|

"""


def remove_column(matrix, col_to_remove):
    return [row[:col_to_remove] + row[col_to_remove + 1:] for row in matrix]


def remove_row(matrix, row_to_remove):
    return [row for i, row in enumerate(matrix) if i != row_to_remove]


def max_val(matrix, n, m, el_i=-1, el_j=-1) -> tuple:
    max1 = -1
    max_pos_1 = (0, 0)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] > max1 and (i != el_i or j != el_j):
                max1 = matrix[i][j]
                max_pos_1 = (i, j)
    return max1, max_pos_1


def find_optimal_ban(n, m, matrix):
    opt_row, opt_col = -1, -1
    max1, max_pos_1 = max_val(matrix, n, m)
    element = matrix[max_pos_1[0]][max_pos_1[1]]
    k = matrix[max_pos_1[0]].count(element)
    z = sum(row[max_pos_1[1]] == element for row in matrix)
    flag = True

    if k > z:
        flag = False
        matrix = remove_row(matrix, max_pos_1[0])
        opt_row = max_pos_1[0]
        n -= 1
    elif k < z:
        flag = False
        matrix = remove_column(matrix, max_pos_1[1])
        opt_col = max_pos_1[1]
        m -= 1
    else:
        flag = False
        max2, max_pos_2 = max_val(matrix, n, m, el_i=max_pos_1[0], el_j=max_pos_1[1])
        if max_pos_2[0] == max_pos_1[0]:
            matrix = remove_row(matrix, max_pos_1[0])
            opt_row = max_pos_1[0]
            n -= 1
        elif max_pos_2[1] == max_pos_1[1]:
            matrix = remove_column(matrix, max_pos_1[1])
            opt_col = max_pos_1[1]
            m -= 1
        else:
            flag = True

    if not flag:
        max2, max_pos_2 = max_val(matrix, n, m, el_i=max_pos_1[0], el_j=max_pos_1[1])
        if opt_row != -1:
            opt_col = max_pos_2[1]
        elif opt_col != -1:
            opt_row = max_pos_2[0]
    else:
        max2, max_pos_2 = max_val(matrix, n, m, el_i=max_pos_1[0], el_j=max_pos_1[1])

        m1 = remove_row(matrix, max_pos_1[0])
        m1 = remove_column(m1, max_pos_2[1])

        m2 = remove_column(matrix, max_pos_1[1])
        m2 = remove_row(matrix, max_pos_2[0])

        max_m1, _ = max_val(m1, n - 1, m - 1, el_i=max_pos_1[0], el_j=max_pos_1[1])
        max_m2, _ = max_val(m2, n - 1, m - 1, el_i=max_pos_1[0], el_j=max_pos_1[1])

        if max_m1 < max_m2:
            opt_row = max_pos_1[0]
            opt_col = max_pos_2[1]
        else:
            opt_col = max_pos_1[1]
            opt_row = max_pos_2[0]

    return opt_row + 1, opt_col + 1


n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
print(*find_optimal_ban(n, m, a))

