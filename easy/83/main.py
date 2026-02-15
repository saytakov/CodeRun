def check_work(
    count_keys: int,
    strength_keys: list[int],
    count_clicks: int,
    i_clicks: list[int]
):
    result_keys = list(strength_keys)
    for i_click in i_clicks:
        result_keys[i_click - 1] -= 1
    for result in result_keys:
        if result >= 0:
            print('NO')
        else:
            print('YES')


def main():
    with open('input.txt', 'r') as file_in:
        count_keys = int(file_in.readline().strip())
        strength_keys = list(map(int, file_in.readline().strip().split()))
        count_clicks = int(file_in.readline().strip())
        i_clicks = map(int, file_in.readline().strip().split())
    check_work(count_keys, strength_keys, count_clicks, i_clicks)


if __name__ == '__main__':
    main()
