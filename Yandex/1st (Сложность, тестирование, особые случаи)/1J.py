"""

|-----------------------|
|--- time limit: 2 s ---|
|- memory limit: 64 Mb--|
|-----------------------|

"""

import re


def parse_document(filename):
    with open(filename, 'r') as file:
        w, h, c = map(int, file.readline().split())
        document = file.read()
    return w, h, c, document


def extract_image_info(text):
    params = text[7:-1].split()
    return {param.split('=')[0]: param.split('=')[1] for param in params}


# Функция для добавления новой строки с одним фрагментом
def add_new_line(w):
    return [{'start': 0, 'end': w}]


def process_paragraph(ph, w, h, c):
    pattern = r'\(image[^\)]*\)|\S+'  # '\(image[^\)]*\)|\S+'  # '\(image[^\)]*\)|[^\s(]+'
    words = re.findall(pattern, ph)
    print(words)
    elems = []
    current_line, current_position, current_line_height = 0, 0, h
    line_fragments = [[{'start': 0, 'end': w}]]  # Список фрагментов для каждой строки
    line_heights = [h]

    for word in words:
        if "(image" in word:
            image_info = extract_image_info(word)
            print(image_info)
            image_width = int(image_info['width'])
            image_height = int(image_info['height'])
            image_layout = image_info['layout']

            if image_layout == 'embedded':

                placed = False
                while not placed and current_line < len(line_fragments):
                    for fragment in line_fragments[current_line]:
                        if fragment['end'] - fragment['start'] >= image_width:
                            elems.append(
                                ('image-embedded', current_line, fragment['start'], line_heights[current_line]))
                            fragment['start'] += image_width
                            placed = True
                            if image_height > line_heights[current_line]:
                                line_heights[current_line] = image_height
                            break
                    if not placed:
                        current_line += 1
                        if current_line == len(line_fragments):
                            line_fragments.append([{'start': 0, 'end': w}])
                            line_heights.append(h)

            elif image_layout == 'surrounded':

                found_fragment = False
                while not found_fragment and current_line < len(line_fragments):
                    for fragment in line_fragments[current_line]:
                        if fragment['end'] - fragment['start'] >= image_width:
                            elems.append(
                                ('image-surrounded', current_line, fragment['start'], line_heights[current_line]))
                            image_affected_lines = max(1, (image_height // line_heights[current_line]) + (
                                1 if image_height % line_heights[current_line] else 0))

                            # Обновляем фрагменты и высоту строк
                            for i in range(image_affected_lines):
                                if current_line + i >= len(line_fragments):
                                    line_fragments.append([{'start': 0, 'end': w}])
                                    line_heights.append(h)
                                if i == 0:
                                    fragment['start'] += image_width
                                else:
                                    line_fragments[current_line + i].insert(0, {'start': fragment['start'],
                                                                                'end': fragment['start'] + image_width})
                                    line_heights[current_line + i] = max(line_heights[current_line + i], image_height)

                            found_fragment = True
                            break
                    if not found_fragment:
                        current_line += 1
                        if current_line == len(line_fragments):
                            line_fragments.append([{'start': 0, 'end': w}])
                            line_heights.append(h)

            elif image_layout == 'floating':
                dx = int(image_info.get('dx', 0))
                dy = int(image_info.get('dy', 0))

                # Вычисляем начальные координаты рисунка
                image_x = current_position + dx
                image_y = (current_line * h) + dy

                # Корректируем положение, если рисунок выходит за границы страницы
                if image_x < 0:
                    image_x = 0
                elif image_x + image_width > w:
                    image_x = w - image_width

                elems.append(('image-floating', image_x, image_y, image_width, image_height))

        else:

            word_width = len(word) * c
            placed = False
            while not placed and current_line < len(line_fragments):
                for fragment in line_fragments[current_line]:
                    if fragment['end'] - fragment['start'] >= word_width:
                        elems.append((word, current_line, fragment['start'], line_heights[current_line]))
                        fragment['start'] += word_width + c
                        placed = True
                        break
                if not placed:
                    current_line += 1
                    if current_line == len(line_fragments):
                        line_fragments.append([{'start': 0, 'end': w}])
                        line_heights.append(h)

    return elems


def main():
    w, h, c, document = parse_document('input1J.txt')

    paragraphs = re.split(r'\n\s*\n', document)

    for paragraph in paragraphs:
        elements = process_paragraph(paragraph, w, h, c)
        print("Элементы абзаца:", elements)


main()
