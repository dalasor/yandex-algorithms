"""
На шахматной доске стоят слоны и ладьи, необходимо посчитать, сколько клеток не бьется ни одной из фигур.
Шахматная доска имеет размеры 8 на 8. Ладья бьет все клетки горизонтали и вертикали, проходящих через клетку,
где она стоит, до первой встретившейся фигуры. Слон бьет все клетки обеих диагоналей, проходящих через клетку,
где он стоит, до первой встретившейся фигуры.

В первых восьми строках ввода описывается шахматная доска. Первые восемь символов каждой из этих строк описывают
состояние соответствующей горизонтали: символ B (заглавная латинская буква) означает, что в клетке стоит слон,
символ R — ладья, символ * — что клетка пуста. После описания горизонтали в строке могут идти пробелы, однако
длина каждой строки не превышает 250 символов. После описания доски в файле могут быть пустые строки.

|-----------------------|
|--- time limit: 1 s ---|
|- memory limit: 64 Mb--|
|-----------------------|

"""


def change_cells(x: int, y: int, directions: list) -> None:
    for dx, dy in directions:
        x_current, y_current = x, y
        while 0 <= x_current < n and 0 <= y_current < n:
            if board[x_current][y_current] != '*' and (x_current != x or y_current != y):
                break
            beated_cells[x_current][y_current] = True
            x_current += dx
            y_current += dy


board = []
n = 8
line = 0
while line < n:
    stroka = input().rstrip()
    board.append(stroka)
    line += 1

beated_cells = [[False] * n for _ in range(n)]

dirs_rook = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dirs_bishop = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

# Атакауемые клетки меняем с 0 на 1
for x_coord in range(n):
    for y_coord in range(n):
        if board[x_coord][y_coord] == 'R':
            change_cells(x_coord, y_coord, dirs_rook)
        elif board[x_coord][y_coord] == 'B':
            change_cells(x_coord, y_coord, dirs_bishop)


print(sum(1 for x in range(n) for y in range(n) if not beated_cells[x][y]))
