def build_table(table, count_rows, count_columns) -> list[list[int]]:
    result_table = [
        [0 for _ in range(count_columns)] for _ in range(count_rows)
    ]
    for row in range(1, count_rows):
        for col in range(1, count_columns):
            result_table[row][col] = (
                result_table[row][col - 1]
                + result_table[row - 1][col]
                - result_table[row - 1][col - 1]
                + table[row][col]
                )
    return result_table


def search_prefix_sum(table, x1, y1, x2, y2) -> int:
    return (
        table[x2][y2]
        - table[x2][y1 - 1]
        - table[x1 - 1][y2]
        + table[x1 - 1][y1 - 1]
    )


def main():
    with open('input.txt', 'r') as file_in:
        count_rows, count_columns, count_requests = (
            map(int, file_in.readline().strip().split())
        )

        table = []
        for _ in range(count_rows):
            if not table:
                table.append([0] * (count_columns + 1))
            row = [0] + list(map(int, file_in.readline().strip().split()))
            table.append(row)
        prefix_sum_table = build_table(table, count_rows + 1, count_columns + 1)

        for _ in range(count_requests):
            x1, y1, x2, y2 = map(int, file_in.readline().strip().split())
            print(search_prefix_sum(prefix_sum_table, x1, y1, x2, y2))


if __name__ == '__main__':
    main()
