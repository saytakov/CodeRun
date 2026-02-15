from collections import deque


def valid_value(row: int, col: int) -> bool:
    if 0 <= row < 8 and 0 <= col < 8:
        return True
    return False


def serch_merge(
    red_row: int,
    red_col: int,
    green_row: int,
    green_col: int
) -> int:
    chess_table = [[[-1, -1] for _ in range(8)] for _ in range(8)]
    chess_table[red_row][red_col][0] = 0
    chess_table[green_row][green_col][1] = 0

    knight_moves = (
        (-2, 1), (-2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2), (2, -1), (2, 1)
    )

    queue = deque([(red_row, red_col, 0), (green_row, green_col, 1)])

    while queue:
        info = queue.popleft()
        row = info[0]
        col = info[1]
        color = info[2]
        for move in knight_moves:
            new_row = row + move[0]
            new_col = col + move[1]
            if (
                valid_value(new_row, new_col)
                and chess_table[new_row][new_col][color] == -1
            ):
                chess_table[new_row][new_col][color] = (
                    chess_table[row][col][color] + 1
                )
                if chess_table[new_row][new_col][0] == (
                    chess_table[new_row][new_col][1]
                ):
                    return chess_table[new_row][new_col][0]
                queue.append((new_row, new_col, color))
    return -1


def main():
    with open('input.txt', 'r') as file_in:
        red, green = file_in.readline().strip().split()
        letter_to_i = {
            'a': 0,
            'b': 1,
            'c': 2,
            'd': 3,
            'e': 4,
            'f': 5,
            'g': 6,
            'h': 7,
        }
        red_row, red_col = int(red[1]) - 1, letter_to_i[red[0]]
        green_row, green_col = int(green[1]) - 1, letter_to_i[green[0]]

        result = serch_merge(red_row, red_col, green_row, green_col)

        print(result)


if __name__ == '__main__':
    main()
