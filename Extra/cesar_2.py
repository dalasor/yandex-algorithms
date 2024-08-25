# Алфавит
en_alphabet = [chr(i) for i in range(65, 91)] + [chr(j) for j in range(97, 123)]


# Сама функция Цезаря для en
def encrypt(text):
    result = ""
    words = text.split()
    for word in words:
        shift = len([e for e in word if e.isalnum()])
        for m in word:
            if m.isalpha():
                if m.isupper():
                    result += en_alphabet[(en_alphabet.index(m) + shift) % 26]
                else:
                    result += en_alphabet[
                        (en_alphabet.index(m) + shift) % 26 + 26
                    ]
            else:
                result += m
        result += ' '

    return result


print(encrypt(input()))
