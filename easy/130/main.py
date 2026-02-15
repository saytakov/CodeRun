def histogram(strokes: list[str]):
    chars_count: dict[str, int] = {}
    for stroke in strokes:
        stroke = stroke.strip().replace(' ', '').replace('\n', '')
        for char in stroke:
            if char in chars_count:
                chars_count[char] += 1
            else:
                chars_count[char] = 1
    chars = sorted(chars_count.keys())
    cur_high = max(chars_count.values())
    for _ in range(cur_high):
        print_res = ''
        for char in chars:
            if chars_count[char] == cur_high:
                print_res += '#'
                chars_count[char] -= 1
            else:
                print_res += ' '
        cur_high -= 1
        print(print_res)
    print(''.join(chars))


def main():
    with open('input.txt', 'r') as file_in:
        strokes = file_in.readlines()
    histogram(strokes)


if __name__ == '__main__':
    main()
