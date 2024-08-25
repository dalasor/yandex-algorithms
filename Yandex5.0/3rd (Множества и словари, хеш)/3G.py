"""
Задано множество, состоящее из N различных точек на плоскости. Координаты всех точек — целые числа.
Определите, какое минимальное количество точек нужно добавить во множество, чтобы нашлось четыре точки,
лежащие в вершинах квадрата.

В первой строке вводится число N (1 ≤ N ≤ 2000) — количество точек. В следующих N строках вводится по два числа
 xi, yi (-10^8 ≤ xi, yi ≤ 10^8) — координаты точек.

Формат вывода

В первой строке выведите число K — минимальное количество точек, которые нужно добавить
во множество. В следующих K строках выведите координаты добавленных точек xi, yi через пробел.
Координаты должны быть целыми и не превышать 10^9 по модулю. Если решений несколько — выведите любое из них.

|-----------------------|
|--- time limit: 2 s ---|
|- memory limit: 256 Mb-|
|-----------------------|
"""

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
points_set = set(points)
x0, y0 = points[0]
ans = [(x0 + 1, y0 + 1), (x0 + 1, y0), (x0, y0 + 1)]
for i in range(n):
    if not ans:
        break
    for j in range(n):
        if i != j:
            x1, y1 = points[i]
            x2, y2 = points[j]
            dx = x2 - x1
            dy = y2 - y1

            x3 = x1 + dy
            y3 = y1 - dx
            x4 = x3 + dx
            y4 = y3 + dy

            if (x3, y3) in points and (x4, y4) in points:
                ans = []
                break
            if len(ans) > 1 and (x3, y3) in points:
                ans = [(x4, y4)]
            if len(ans) > 1 and (x4, y4) in points:
                ans = [(x3, y3)]
            if len(ans) > 2:
                ans = [(x3, y3), (x4, y4)]

print(len(ans))
for an in ans:
    print(*an)

# x, y = zip(*points)
# plt.scatter(x, y, color='blue', label='Original Points')
# plt.grid(which='both', linestyle='--', linewidth=0.5)
# plt.xticks(range(min(x) - 1, max(x) + 2))
# plt.yticks(range(min(y) - 1, max(y) + 2))
# plt.show()


# def find_min(points):
#     existing_points_set = set(points)
#     min_additional_points = float('inf')
#     best_solution = []
#
#     # Проверяем каждую пару точек
#     for i in range(len(points)):
#         for j in range(i + 1, len(points)):
#             x1, y1 = points[i]
#             x2, y2 = points[j]
#
#             # Случай, когда точки на диагонали квадрата
#             if abs(x1 - x2) == abs(y1 - y2):
#                 options = [
#                     [(x1, y2), (x2, y1)]
#                 ]
#
#             # Поиск потенциальных точек для всех четырех направлений
#             elif y1 == y2:  # Горизонтальная линия
#                 dist = abs(x1 - x2)
#                 options = [
#                     [(x1, y1 + dist), (x2, y2 + dist)],  # Вверх
#                     [(x1, y1 - dist), (x2, y2 - dist)]  # Вниз
#                 ]
#             elif x1 == x2:  # Вертикальная линия
#                 dist = abs(y1 - y2)
#                 options = [
#                     [(x1 + dist, y1), (x2 + dist, y2)],  # Вправо
#                     [(x1 - dist, y1), (x2 - dist, y2)]  # Влево
#                 ]
#             else:  # Диагональ или неподходящая пара точек
#                 continue
#
#             # Выбираем оптимальный набор точек
#             for option in options:
#                 missing = [pt for pt in option if pt not in existing_points_set]
#                 if len(missing) == 0:
#                     return []
#                 elif 0 < len(missing) < min_additional_points:
#                     min_additional_points = len(missing)
#                     best_solution = missing
#
#     return best_solution
