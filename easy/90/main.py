def minimal_difference(colors_tshirt, colors_shorts, count_color_tshirt, count_color_shorts):
    cursor_tshirt = 0
    cursor_shorts = 0
    min_dif = 100000000000000000000000000000000
    result_tshirt = 0
    result_shorts = 0
    while True:
        if cursor_tshirt == count_color_tshirt:
            cursor_tshirt -= 1
            break
        if cursor_shorts == count_color_shorts:
            cursor_shorts -= 1
            break
        cur_diff = abs(colors_tshirt[cursor_tshirt] - colors_shorts[cursor_shorts])
        if cur_diff < min_dif:
            min_dif = cur_diff
            result_tshirt = colors_tshirt[cursor_tshirt]
            result_shorts = colors_shorts[cursor_shorts]
        if colors_tshirt[cursor_tshirt] == colors_shorts[cursor_shorts]:
            result_tshirt = colors_tshirt[cursor_tshirt]
            result_shorts = colors_shorts[cursor_shorts]
            break
        elif colors_tshirt[cursor_tshirt] < colors_shorts[cursor_shorts]:
            cursor_tshirt += 1
        elif colors_tshirt[cursor_tshirt] > colors_shorts[cursor_shorts]:
            cursor_shorts += 1
    return result_tshirt, result_shorts


def main():
    with open('input.txt', 'r') as file_in:
        count_color_tshirt = int(file_in.readline().strip())
        colors_tshirt = list(map(int, file_in.readline().strip().split()))
        count_color_shorts = int(file_in.readline().strip())
        colors_shorts = list(map(int, file_in.readline().strip().split()))
    result = minimal_difference(colors_tshirt, colors_shorts, count_color_tshirt, count_color_shorts)
    print(' '.join(map(str, result)))


if __name__ == '__main__':
    main()
