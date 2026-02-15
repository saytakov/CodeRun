def search_count(stroke: list[str]) -> str:
    counts: dict[str, int] = {}
    result = ''

    for word in stroke:
        if word not in counts:
            counts[word] = 0
        else:
            counts[word] += 1
        result += f'{counts[word]} '

    return result


def main():
    with open('input.txt', 'r') as file_in:
        strokes = file_in.read()
    result = search_count(strokes.strip().split())
    print(result)


if __name__ == '__main__':
    main()
