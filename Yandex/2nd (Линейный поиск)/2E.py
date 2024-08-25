"""
Домашний питомец мальчика Васи — улитка Петя. Петя обитает на бесконечном в обе стороны вертикальном столбе,
который для удобства можно представить как числовую прямую. Изначально Петя находится в точке 0.
Вася кормит Петю ягодами. У него есть n ягод, каждая в единственном экземпляре. Вася знает, что если утром он
даст Пете ягоду с номером i, то поев и набравшись сил, за остаток дня Петя поднимется на a i единиц вверх по
столбу, но при этом за ночь, потяжелев, съедет на b i единиц вниз. Параметры различных ягод могут совпадать.
Пете стало интересно, а как оно там, наверху, и Вася взялся ему в этом помочь. Ближайшие n дней он будет
кормить Петю ягодами из своего запаса таким образом, чтобы максимальная высота, на которой побывал Петя
за эти n дней была максимальной. К сожалению, Вася не умеет программировать, поэтому он попросил вас о помощи.
Найдите, максимальную высоту, на которой Петя сможет побывать за эти n дней и в каком порядке Вася должен
давать Пете ягоды, чтобы Петя смог её достичь!

В первой строке выходных данных выведите единственное число — максимальную высоту, которую сможет достичь Петя,
если Вася будет его кормить оптимальным образом. В следующей строке выведите n различных целых чисел
от 1 до n  — порядок, в котором Вася должен кормить Петю (i число в строке соответствует номеру ягоды,
которую Вася должен дать Пете в i день чтобы Петя смог достичь максимальной высоты).

|-----------------------|
|--- time limit: 5 s ---|
|- memory limit: 256 Mb--|
|-----------------------|

"""

n = int(input())
a, b = [], []
for i in range(1, n + 1):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

max_sum = 0
max_ind = 0
s = 0
for i in range(n):
    if a[i] - b[i] > 0:
        s += a[i] - b[i]

for i in range(n):
    ns = s
    s += b[i] if a[i] - b[i] > 0 else a[i]
    if s > max_sum:
        max_sum = s
        max_ind = i
    s = ns

print(max_sum)

order = ([i + 1 for i in range(n) if a[i] - b[i] > 0 and i != max_ind] + [max_ind + 1] +
         [i + 1 for i in range(n) if a[i] - b[i] <= 0 and i != max_ind])

print(*order)



