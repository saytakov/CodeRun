def valid_value(row, col, max_row, max_col):
    if 0 <= row < max_row and 0 <= col < max_col:
        return True
    return False


def main():
    with open('input.txt', 'r') as file_in:
        count_row, count_col, count_min = map(
            int,
            file_in.readline().strip().split()
        )
        table_saper = [[0 for _ in range(count_col)] for _ in range(count_row)]
        numbers_mins = (
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        )
        for _ in range(count_min):
            row, col = map(int, file_in.readline().strip().split())
            table_saper[row-1][col-1] = '*'
            for row_move, col_move in numbers_mins:
                new_row = row + row_move - 1
                new_col = col + col_move - 1
                if (
                    valid_value(new_row, new_col, count_row, count_col)
                    and table_saper[new_row][new_col] != '*'
                ):
                    table_saper[new_row][new_col] += 1
        for i in range(count_row):
            print(' '.join(map(str, table_saper[i])))


if __name__ == '__main__':
    main()
