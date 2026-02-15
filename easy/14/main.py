import sys
from collections import deque
from pprint import pprint


def valid_value(row: int, col: int, rows_board: int, cols_board: int) -> bool:
    if 0 <= row < rows_board and 0 <= col < cols_board:
        return True
    return False


def count_jumps(
    rows_board: int,
    cols_board: int,
    row_feeder: int,
    col_feeder: int,
    count_fleas: int,
    coordinates_fleas: list[tuple[int, int]]
):
    board = [[-1 for _ in range(cols_board)] for _ in range(rows_board)]
    board[row_feeder][col_feeder] = 0
    knight_moves: tuple[tuple[int, int], ...] = (
        (-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)
    )
    queue = deque([(row_feeder, col_feeder)])

    while queue:
        row, col = queue.popleft()

        for knight_move_row, knight_move_col in knight_moves:
            new_row, new_col = row + knight_move_row, col + knight_move_col

            if (
                valid_value(new_row, new_col, rows_board, cols_board)
                and board[new_row][new_col] == -1
            ):
                board[new_row][new_col] = board[row][col] + 1
                queue.append((new_row, new_col))
    pprint(board)

    result = 0

    for row_flea, col_flea in coordinates_fleas:
        jumps = board[row_flea][col_flea]
        if jumps == -1:
            return -1
        result += jumps

    return result


def main():
    # with open('input.txt', 'r') as file_in:
    #     coordinates_fleas: list[tuple[int, int]] = []
    #     rows_board, cols_board, row_feeder, col_feeder, count_fleas = list(map(
    #         int, file_in.readline().strip().split()
    #     ))
    #     for i in range(count_fleas):
    #         coordinates_fleas.append(tuple(
    #             map(lambda x: int(x)-1, file_in.readline().strip().split())
    #         ))
    coordinates_fleas: list[tuple[int, int]] = []
    rows_board, cols_board, row_feeder, col_feeder, count_fleas = list(map(
        int, sys.stdin.readline().strip().split()
    ))
    for i in range(count_fleas):
        coordinates_fleas.append(tuple(
            map(lambda x: int(x)-1, sys.stdin.readline().strip().split())
        ))

    result = count_jumps(
        rows_board,
        cols_board,
        row_feeder-1,
        col_feeder-1,
        count_fleas,
        coordinates_fleas
    )
    print(result)


if __name__ == '__main__':
    main()
