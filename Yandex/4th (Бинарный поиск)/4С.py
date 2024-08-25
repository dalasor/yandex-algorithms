""" Зашло на PyPy"""

"""
Как известно, Саруман Радужный очень любит порядок. Поэтому все полки его войска стоят друг за другом, 
причем каждый следующий полк содержит количество орков не меньше, чем предыдущий.

Перед тем как напасть на Хельмову Падь, Саруман решил провести несколько вылазок для разведки. 
Чтобы его отряды никто не заметил, он решил каждый раз отправлять несколько подряд идущих полков 
так, чтобы суммарное количество орков в них было равно определенному числу. 
Так как это всего лишь разведка, каждый полк после вылазки возвращается на свое место. 
Задачу выбрать нужные полки он поручил Гриме Змеиному Языку. А Грима не поскупится на вознаграждение, 
если вы ему поможете.

Для каждого запроса выведите номер полка, с которого начнутся те l, которые необходимо отправить на вылазку. 
Если таких полков несколько, выведите любой. Если же так выбрать полки нельзя, выведите -1.

|-----------------------|
|--- time limit: 4 s ---|
|- memory limit: 256 Mb |
|-----------------------|

"""


def prefix_sums(orks):
    sums = [0]
    for o in orks:
        sums.append(sums[-1] + o)
    return sums


def find_ind(n, pref_sums, polks, s):
    left, right = 0, n - polks
    while left <= right:
        mid = (left + right) // 2
        current_sum = pref_sums[mid + polks] - pref_sums[mid]
        if current_sum == s:
            return mid + 1
        elif current_sum < s:
            left = mid + 1
        else:
            right = mid
    return -1


n, m = map(int, input().split())
orks = list(map(int, input().split()))
pref_sums = prefix_sums(orks)
print(pref_sums)
for _ in range(m):
    polks, s = map(int, input().split())
    print(find_ind(n, pref_sums, polks, s))

