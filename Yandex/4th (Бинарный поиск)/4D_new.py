def test_find_min_roll_length() -> None:
    assert find_min_roll_length(15, [2, 2, 2, 3, 2, 2], [3, 3, 5, 2, 4, 3]) == 3
    assert find_min_roll_length(15, [1, 1], [3, 3, 5, 2, 4, 3]) == 2
    assert find_min_roll_length(10, [1, 1, 2, 1, 2], [7, 7, 1, 5, 5]) == 4
    assert find_min_roll_length(10, [1, 1, 1, 1, 1], [5, 2, 3, 3, 4]) == 4


def place_report(report: list[int], width: int) -> int:
    cur_line = 0
    cur_col = 0
    i = 0
    while i < len(report):
        if cur_col + report[i] > width:
            cur_col = 0
            cur_line += 1
            continue

        cur_col += report[i] + 1
        i += 1

    return cur_line + 1


def find_min_roll_length(roll_width: int, first_report: list[int], second_report: list[int]) -> int:
    low, high = max(first_report), roll_width - max(second_report)

    min_length = None
    while low < high:
        middle = (low + high) // 2
        first_length = place_report(first_report, middle)
        second_length = place_report(second_report, roll_width - middle)
        candidate = max(first_length, second_length)
        if min_length is None or candidate < min_length:
            min_length = candidate

        if first_length > second_length:
            low = middle + 1
        elif second_length > first_length:
            high = middle - 1
        else:
            return first_length

    first_length = place_report(first_report, low)
    second_length = place_report(second_report, roll_width - low)
    candidate = max(first_length, second_length)
    if min_length is None or candidate < min_length:
        min_length = candidate

    return min_length


def main() -> None:
    w, _, _ = map(int, input().split())
    first_report = list(map(int, input().split()))
    second_report = list(map(int, input().split()))
    print(find_min_roll_length(w, first_report, second_report))


if __name__ == "__main__":
    main()
