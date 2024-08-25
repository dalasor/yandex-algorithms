# Сумма всех цифр страниц в книге с N страниц
def count(n: int) -> int:
    s = 0
    for j in range(1, n + 1):
        z = j
        while z > 0:
            s += z % 10
            z = z // 10
    return s


# Сумма КОЛИЧЕСТВА всех цифр страниц в книге с N страниц
def count_new(n: int) -> int:
    s = 0
    for j in range(1, n + 1):
        z = j
        while z > 0:
            s += 1
            z = z // 10
    return s


n = int(input())
i = 1
s = 0
while s < 1095:
    k = i
    while k > 0:
        s += 1
        k = k // 10
    i += 1

print('Количество страниц:', i - 1)
print('Сумма:', s)

print('Проверка при n =', n, ':', count_new(n))
