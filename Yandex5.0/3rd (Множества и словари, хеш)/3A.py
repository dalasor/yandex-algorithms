"""
Костя успешно прошел собеседование и попал на стажировку в отдел разработки сервиса «Музыка».
Конкретно ему поручили такое задание — научиться подбирать плейлист для группы друзей,
родственников или коллег. При этом нужно подобрать такой плейлист, в который входят
исключительно нравящиеся всем членам группы песни.
Костя очень хотел выполнить это задание быстро и качественно, но у него не получается.
Помогите ему написать программу, которая составляет плейлист для группы людей.

В первой строке расположено одно натуральное число n (1 ≤ n ≤ 2*10^5), где n – количество человек в группе.
В следующих 2 ⋅ n строках идет описание любимых плейлистов членов группы. По 2 строки на каждого участника.
В первой из этих 2 -х строк расположено число k_i — количество любимых треков i -го члена группы.
В следующей строке расположено k_i строк через пробел — названия любимых треков i -го участника группы.
Каждый трек в плейлисте задан в виде строки, все строки уникальны, сумма длин строк не превосходит 2*10^6.
Строки содержат большие и маленькие латинские буквы и цифры.

Выведите количество, а затем сам список песен через пробел — список треков, которые нравятся каждому участнику группы.
Ответ необходимо отсортировать в лексикографическом порядке

|-----------------------|
|--- time limit: 1 s ---|
|- memory limit: 256 Mb-|
|-----------------------|

"""


def create_playlist(n, groups):
    track_counts = {}
    for tracks in groups:
        for track in tracks:
            track_counts[track] = track_counts.get(track, 0) + 1

    common_tracks = [track for track, count in track_counts.items() if count == n]
    common_tracks.sort()
    return len(common_tracks), common_tracks


n = int(input())
groups = []
for _ in range(n):
    _ = input()
    group_tracks = input().split()
    groups.append(group_tracks)

playlist_count, playlist = create_playlist(n, groups)
print(playlist_count)
print(' '.join(playlist))

