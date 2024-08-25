# Алфавиты
en_alphabet = [chr(i) for i in range(65, 91)] + [chr(j) for j in range(97, 123)]
ru_alphabet = [chr(i) for i in range(1040, 1104)]


# Шифрование или Дешифрование
def shifr_vvodim():
    while True:
        shifr = input("Чем сегодня займемся? Шифрованием или дешифрованием? (ш/д)\n")
        if shifr in ("ш", "Ш"):
            return 1
        if shifr in ("д", "Д"):
            return -1
        else:
            print("Что-то ты ввел не то, попробуй ещё раз")
            continue


# Решаем какой будет сдвиг
def sdvig_caesar():
    while True:
        sdvig = input("Какой будет сдвиг?\n")
        if sdvig.isdigit():
            return int(sdvig)
        else:
            sdvig = int(input("Ты ввел не число, попробуй снова \n"))
            continue


# Сама функция Цезаря для двух языков, с выводом значений, если они не соответсвуют языку
def Shifr_Caesar(shifr, sdvig, text):
    result = ""
    for m in text:
        if m.isalpha():
            if m in en_alphabet:
                if m.isupper():
                    result += en_alphabet[(en_alphabet.index(m) + sdvig * shifr) % 26]
                else:
                    result += en_alphabet[
                        (en_alphabet.index(m) + sdvig * shifr) % 26 + 26
                    ]
            if m in ru_alphabet:
                if m.isupper():
                    result += ru_alphabet[(ru_alphabet.index(m) + sdvig * shifr) % 32]
                else:
                    result += ru_alphabet[
                        (ru_alphabet.index(m) + sdvig * shifr) % 32 + 32
                    ]
        else:
            result += m

    return result


while True:
    print(Shifr_Caesar(shifr_vvodim(), sdvig_caesar(), input("Введите текст\n")))
    if input("Повторить?\n").lower() == "нет":
        print('До скорых встреч!')
        break
