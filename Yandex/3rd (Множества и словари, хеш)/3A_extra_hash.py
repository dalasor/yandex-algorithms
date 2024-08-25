# Решение ооооочень медленное, встроенные возможности быстрее

class HashTable:
    def __init__(self, size=10000):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.prime = 1000000007  # Большое простое число

    # def hash_function(self, key):
    #     return sum(ord(char) for char in key) % self.size

    def hash_function(self, key):
        hash_value = 0
        p = 31  # Маленькое простое число, основание полиномиального хэширования
        p_pow = 1
        for char in key:
            hash_value = (hash_value + (ord(char) - ord('a') + 1) * p_pow) % self.prime
            p_pow = (p_pow * p) % self.prime
        return hash_value % self.size

    def add(self, key):
        hash_key = self.hash_function(key)
        if key not in self.table[hash_key]:
            self.table[hash_key].append(key)

    def contains(self, key):
        hash_key = self.hash_function(key)
        return key in self.table[hash_key]


def create_playlist(n, groups):
    hash_tables = [HashTable() for _ in range(n)]
    for i, tracks in enumerate(groups):
        for track in tracks:
            hash_tables[i].add(track)

    # Находим общие треки
    common_tracks = set(hash_tables[0].table[hash_key][0] for hash_key in range(hash_tables[0].size) if hash_tables[0].table[hash_key])
    for i in range(1, n):
        common_tracks.intersection_update(set(hash_tables[i].table[hash_key][0] for hash_key in range(hash_tables[i].size) if hash_tables[i].table[hash_key]))

    common_tracks = sorted(common_tracks)
    return len(common_tracks), common_tracks


# Чтение входных данных
n = int(input())
groups = []
for _ in range(n):
    _ = input()  # Пропускаем количество треков, так как оно не нужно
    group_tracks = input().split()
    groups.append(group_tracks)

# Создание плейлиста
playlist_count, playlist = create_playlist(n, groups)
print(playlist_count)
print(' '.join(playlist))
