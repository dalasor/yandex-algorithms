"""
Из шахматной доски по границам клеток выпилили связную (не распадающуюся на части) фигуру без дыр.
Требуется определить ее периметр.

Формат ввода
Сначала вводится число N (1 ≤ N ≤ 64) – количество выпиленных клеток. В следующих N строках
вводятся координаты выпиленных клеток, разделенные пробелом (номер строки и столбца – числа от 1 до 8).
Каждая выпиленная клетка указывается один раз.

Формат вывода
Выведите одно число – периметр выпиленной фигуры (сторона клетки равна единице).

|-----------------------|
|--- time limit: 1 s ---|
|- memory limit: 64 Mb--|
|-----------------------|

"""


def calculate_perimeter(n: int, cut_cells: list) -> int:
    cells = set(cut_cells)
    perimeter = 4 * n
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for cell in cells:
        for dx, dy in directions:
            neighbor = (cell[0] + dx, cell[1] + dy)
            if neighbor in cells:
                perimeter -= 1

    return perimeter


n = int(input())
xys = []
for i in range(n):
    xys.append(tuple(map(int, input().split())))

print(calculate_perimeter(n, xys))
