"""
Дан массив целых положительных чисел a длины n. Разбейте его на минимально возможное количество отрезков,
чтобы каждое число было не меньше длины отрезка которому оно принадлежит. Длиной отрезка считается количество
чисел в нем.

Разбиение массива на отрезки считается корректным, если каждый элемент принадлежит ровно одному отрезку.

|-----------------------|
|--- time limit: 2 s ---|
|- memory limit: 256 Mb-|
|-----------------------|
"""


def split_array(n, array):
    segments = []
    segments_lists = []
    start = 0

    while start < n:
        length = 1
        current_min = array[start]
        while start + length <= n and current_min >= length:
            if start + length < n:
                current_min = min(current_min, array[start + length])
            length += 1
        segments.append(length - 1)
        segments_lists.append(array[start:start + length - 1])
        start += length - 1

    return len(segments), segments, segments_lists


t = int(input())
for _ in range(t):
    n = int(input())
    m = list(map(int, input().split()))
    seg_num, seg_seq, segs = split_array(n, m)
    print(seg_num)
    print(*seg_seq)
