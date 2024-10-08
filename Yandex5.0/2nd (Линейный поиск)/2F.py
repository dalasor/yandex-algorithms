"""
Развлекательный телеканал транслирует шоу «Колесо Фортуны». В процессе игры участники шоу крутят большое колесо,
разделенное на сектора. В каждом секторе этого колеса записано число. После того как колесо останавливается,
специальная стрелка указывает на один из секторов. Число в этом секторе определяет выигрыш игрока.
Юный участник шоу заметил, что колесо в процессе вращения замедляется из-за того, что стрелка задевает
за выступы на колесе, находящиеся между секторами. Если колесо вращается с угловой скоростью v градусов
в секунду, и стрелка, переходя из сектора X к следующему сектору, задевает за очередной выступ,
то текущая угловая скорость движения колеса уменьшается на k градусов в секунду. При этом если v ≤ k,
то колесо не может преодолеть препятствие и останавливается. Стрелка в этом случае будет указывать на сектор X.

Юный участник шоу собирается вращать колесо. Зная порядок секторов на колесе, он хочет заставить колесо
вращаться с такой начальной скоростью, чтобы после остановки колеса стрелка указала на как можно
большее число. Колесо можно вращать в любом направлении и придавать ему начальную угловую скорость
от a до b градусов в секунду.

Требуется написать программу, которая по заданному расположению чисел в секторах, минимальной и максимальной
начальной угловой скорости вращения колеса и величине замедления колеса при переходе через границу
секторов вычисляет максимальный выигрыш.

|-----------------------|
|--- time limit: 1 s ---|
|- memory limit: 64 Mb--|
|-----------------------|

"""

def max_win(values, count) -> int:
    return max(values[count % n], values[-count % n])


n = int(input())
values = list(map(int, input().split()))
a, b, k = map(int, input().split())

max_val = max(values)
max_cur, max_i = 0, 0
count = 0
i = a

while a <= i <= b:
    count = i // k
    count -= 1 if i % k == 0 else 0
    while count > n:
        count = count % n
    max_i = max_win(values, count)
    if max_i == max_val:
        max_cur = max_i
        break
    else:
        if max_i > max_cur:
            max_cur = max_i

    i += k - 1 if k > 1 else k

print(max_cur if max_cur != max_val else max_val)
