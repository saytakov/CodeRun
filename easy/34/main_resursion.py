def search_path(stroke: str, count: int, steps: dict[str, str]) -> int:
    if count == 1:
        return len(stroke)
    else:
        result = 0
        for value in stroke:
            result += 1 + search_path(steps[value], count - 1, steps)
        return result


def main():
    with open('input.txt', 'r') as file_in:
        steps = {
            'N': '',
            'S': '',
            'W': '',
            'E': '',
            'U': '',
            'D': ''
        }
        steps['N'] = file_in.readline().strip()
        steps['S'] = file_in.readline().strip()
        steps['W'] = file_in.readline().strip()
        steps['E'] = file_in.readline().strip()
        steps['U'] = file_in.readline().strip()
        steps['D'] = file_in.readline().strip()
        start, count = file_in.readline().strip().split()
        count = int(count)

    result = search_path(start, count, steps)
    print(result)


if __name__ == '__main__':
    main()
