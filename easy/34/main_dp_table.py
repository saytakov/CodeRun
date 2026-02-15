def search_path(steps: dict[str, str], count: int, start) -> int:
    direction_to_i: dict[str, int] = {
        'N': 0, 'S': 1, 'W': 2, 'E': 3, 'U': 4, 'D': 5
    }

    i_to_direction: dict[int, str] = {
        0: 'N', 1: 'S', 2: 'W', 3: 'E', 4: 'U', 5: 'D'
    }

    dp_table: list[list[int]] = [
        [0 for _ in range(count + 1)] for _ in range(6)
    ]

    for i in range(6):
        dp_table[i][1] = 1

    for i in range(2, count + 1):
        for j in range(6):
            cur_direction: str = i_to_direction[j]
            summ: int = 1
            for direction in steps[cur_direction]:
                summ += dp_table[direction_to_i[direction]][i - 1]
            dp_table[j][i] = summ

    return dp_table[direction_to_i[start]][count]


def main():
    with open('input.txt', 'r') as file_in:
        steps: dict[str, str] = {
            'N': file_in.readline().strip(),
            'S': file_in.readline().strip(),
            'W': file_in.readline().strip(),
            'E': file_in.readline().strip(),
            'U': file_in.readline().strip(),
            'D': file_in.readline().strip()
        }
        start, count = file_in.readline().strip().split()

    result: int = search_path(steps, int(count), start)

    print(result)


if __name__ == '__main__':
    main()
