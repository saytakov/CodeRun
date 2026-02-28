def dp(table, n, m):
    result_table = [[0 for _ in range(m)] for _ in range(n)]
    result_table[0][0] = table[0][0]
    for i in range(1, m):
        result_table[0][i] = result_table[0][i - 1] + table[0][i]
    for i in range(1, n):
        result_table[i][0] = result_table[i - 1][0] + table[i][0]
    for row in range(1, n):
        for col in range(1, m):
            result_table[row][col] = (
                min(result_table[row - 1][col], result_table[row][col - 1])
                + table[row][col]
            )
    return result_table[-1][-1]


def main():
    with open('input.txt', 'r') as file_in:
        n, m = map(int, file_in.readline().strip().split())
        table = tuple(tuple(map(int, file_in.readline().strip().split())) for _ in range(n))
    print(dp(table, n, m))


if __name__ == '__main__':
    main()
