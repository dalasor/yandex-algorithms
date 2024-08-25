# ПРАВИЛЬНАЯ СКОБОЧНАЯ ПОСЛЕДОВАТЕЛЬНОСТЬ

# 1-ый вариант, когда нам важен сам факт - правильная или неправильная

# seq = input()  # скобочная последовательность
# stack = []
# is_good = True
# for elem in seq:
#     if elem in '({[':
#         stack.append(elem)
#     elif elem in ')}]':
#         if not stack:
#             is_good = False
#             break
#         last = stack.pop()
#         if last == '(' and elem == ')':
#             continue
#         elif last == '[' and elem == ']':
#             continue
#         elif last == '{' and elem == '}':
#             continue
#         else:
#             is_good = False
#             break
#
# print('OK' if is_good else 'NOT OK')


# 2 - когда нас интересует именно та скобка, на которой мы поняли, что все сломалось

# объявление функции
def verification(text: str) -> int:
    stack = []
    for i, elem in enumerate(text):
        if elem in '({[':
            stack.append((elem, i + 1))
        elif elem in ')}]':
            if not stack:
                return i + 1
            last = stack.pop()
            if ((last[0] == '(' and elem == ')')
                    or (last[0] == '[' and elem == ']')
                    or (last[0] == '{' and elem == '}')):
                continue
            else:
                return i + 1

    if stack:
        return stack[0][1]
    else:
        return 0


# считываем данные
txt = input()

# вызываем функцию
done = verification(txt)
print('Success' if done == 0 else done)

# assert verification("([](){([])})") == 0
# assert verification("()[]}") == 5
# assert verification("{{[()]]") == 7
# assert verification("{{{[][][]") == 3
# assert verification("{*{{}") == 3
# assert verification("[[*") == 2
# assert verification("{*}") == 0
# assert verification("{{") == 2
# assert verification("{}") == 0
# assert verification("") == 0
# assert verification("}") == 1
# assert verification("*{}") == 0
# assert verification("{{{**[][][]") == 1
# assert verification('()({}') == 3
# assert verification('{{[()]}') == 1
# assert verification('[]') == 0
# assert verification('{}[]') == 0
# assert verification('[()]') == 0
# assert verification('(())') == 0
# assert verification('{[]}()') == 0
# assert verification('([](){([])})') == 0
# assert verification('foo(bar);') == 0
# assert verification('{') == 1
# assert verification('{[}') == 3
# assert verification('()[]}') == 5
# assert verification('{{[()]]') == 7
# assert verification('foo(bar[i);') == 10
# assert verification('[]([]') == 3
# assert verification('{{{') == 1
