import sys
from collections import deque
from pprint import pprint


def valid_coordinates(floor, row, col, max_len):
    if (
        0 <= floor < max_len
        and 0 <= row < max_len
        and 0 <= col < max_len
    ):
        return True
    return False


def search_path(
    blocks: list[list[list[int]]],
    count_blocks: int,
    start: tuple[int, int, int]
) -> int:
    steps = []
    for position in range(-1, 2):
        for direction in range(-1, 2, 2):
            step = [0, 0, 0]
            step[position] = direction
            steps.append(step)

    queue = deque([start])

    while queue:
        floor, row, col = queue.popleft()

        for floor_step, row_step, col_step in steps:
            new_floor_step, new_row_step, new_col_step = (
                floor + floor_step,
                row + row_step,
                col + col_step
            )

            if (
                valid_coordinates(
                    new_floor_step,
                    new_row_step,
                    new_col_step,
                    count_blocks
                )
                and blocks[new_floor_step][new_row_step][new_col_step] == -1
            ):
                blocks[new_floor_step][new_row_step][new_col_step] = (
                    blocks[floor][row][col] + 1
                )

                queue.append((new_floor_step, new_row_step, new_col_step))

    result = sys.maxsize

    for i in range(count_blocks):
        for j in range(count_blocks):
            if blocks[0][i][j] > 0:
                result = min(result, blocks[0][i][j])

    return result


def main():
    count_blocks = int(sys.stdin.readline().strip())
    blocks = []
    for i in range(count_blocks):
        sys.stdin.readline()
        block = []
        blocks.append(block)
        for j in range(count_blocks):
            row = list(map(
                    int,
                    sys.stdin.readline()
                    .replace('#', '-2 ')
                    .replace('.', '-1 ')
                    .replace('S', '0 ')
                    .strip()
                    .split()
            ))
            block.append(row)
            if 0 in row:
                start = (i, j, row.index(0))
    result = search_path(blocks, count_blocks, start)
    print(result)
    # with open('input.txt', 'r') as file_in:
    #     count_blocks = int(file_in.readline().strip())
    #     blocks = []
    #     for i in range(count_blocks):
    #         file_in.readline()
    #         block = []
    #         blocks.append(block)
    #         for j in range(count_blocks):
    #             row = list(map(
    #                     int,
    #                     file_in.readline()
    #                     .replace('#', '-2 ')
    #                     .replace('.', '-1 ')
    #                     .replace('S', '0 ')
    #                     .strip()
    #                     .split()
    #             ))
    #             block.append(row)
    #             if 0 in row:
    #                 start = (i, j, row.index(0))
    # result = search_path(blocks, count_blocks, start)
    # print(result)


if __name__ == '__main__':
    main()
