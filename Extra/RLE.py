def rle(s):
    def pack(s, cnt):
        return s + str(cnt)

    lastsym = s[0]
    lastpos = 0
    ans = []
    for i in range(len(s)):
        if s[i] != lastsym:
            ans.append(pack(lastsym, i - lastpos))
            lastpos = i
            lastsym = s[i]

    ans.append(pack(s[lastpos], len(s) - lastpos))
    return ''.join(ans)


def create_dict(s) -> dict:
    d = dict()
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i] in d.keys():
                d[s[i]] += int(s[i + 1])
            else:
                d[s[i]] = int(s[i + 1])

    return d


def countindict(s: str) -> dict:
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


s = 'AAABBBBBBCDDCCCCDDDDAAAAAABBB'
news = rle(s)
print(news)
res_dict = create_dict(news)
print(res_dict)
print(countindict(s))
