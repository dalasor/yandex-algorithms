"""
Вася играет в настольную игру «Пираты Баренцева моря», которая посвящена морским битвам.
Игровое поле представляет собой квадрат из N × N клеток, на котором расположено N кораблей
(каждый корабль занимает одну клетку). Вася решил воспользоваться линейной тактикой, для этого
ему необходимо выстроить все N кораблей в одном столбце. За один ход можно передвинуть один корабль
в одну из четырёх соседних по стороне клеток. Номер столбца, в котором будут выстроены корабли,
не важен. Определите минимальное количество ходов, необходимых для построения кораблей в одном столбце.
В начале и процессе игры никакие два корабля не могут находиться в одной клетке.

Формат ввода
В первой строке входных данных задаётся число N (1 ≤ N ≤ 100).
В каждой из следующих N строк задаются координаты корабля: сначала номер строки, затем номер столбца
(нумерация начинается с единицы).

Формат вывода
Выведите одно число — минимальное количество ходов, необходимое для построения.

|-----------------------|
|--- time limit: 1 s ---|
|- memory limit: 64 Mb--|
|-----------------------|

"""

def min_moves(ship_pos, n):
    m = sorted(col for _, col in ship_pos)[n // 2]
    row_counts = {row: 0 for row in range(1, n + 1)}
    for row, _ in ship_pos:
        row_counts[row] += 1

    extra_ships = [row for row, count in row_counts.items() if count > 1 for _ in range(count - 1)]
    empty_rows = [row for row, count in row_counts.items() if count == 0]
    v_moves = sum(abs(es - er) for es, er in zip(extra_ships, empty_rows))

    return sum(abs(col - m) for _, col in ship_pos) + v_moves


n = int(input())
coords = [tuple(map(int, input().split())) for _ in range(n)]
print(min_moves(coords, n))
