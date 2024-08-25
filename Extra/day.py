"""
Задача: найти, сколько раз часы показывают разное время за день
"""
count = 0
for h in range(24):
    h1, h2 = h // 10, h % 10
    for m in range(60):
        m1, m2 = m // 10, m % 10
        if len({h1, h2, m1, m2}) == 4:
            print(h1, h2, ':', m1, m2, sep='')
            count += 1

print(count)
