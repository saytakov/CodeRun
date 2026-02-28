from pprint import pprint


def longest_common_subsequence(first_seq, second_seq, n, m):
    matrix_lcs = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, m + 1):
        if first_seq[0] == second_seq[i-1]:
            matrix_lcs[1][i] = matrix_lcs[0][i - 1] + 1
        else:
            matrix_lcs[1][i] = max(matrix_lcs[0][i], matrix_lcs[1][i-1])
    for i in range(1, n + 1):
        if second_seq[0] == first_seq[i - 1]:
            matrix_lcs[i][1] = matrix_lcs[i - 1][0] + 1
        else:
            matrix_lcs[i][1] = max(matrix_lcs[i][0], matrix_lcs[i - 1][1])

    for row in range(1, n + 1):
        for col in range(1, m + 1):
            if first_seq[row - 1] == second_seq[col - 1]:
                matrix_lcs[row][col] = matrix_lcs[row - 1][col - 1] + 1
            else:
                matrix_lcs[row][col] = max(matrix_lcs[row][col - 1], matrix_lcs[row - 1][col])

    cur_row = n
    cur_col = m
    result_subsequence = []
    while (cur_row - 1 >= 0) and (cur_col - 1 >= 0):
        if matrix_lcs[cur_row][cur_col] == 0:
            break
        if first_seq[cur_row - 1] == second_seq[cur_col - 1]:
            result_subsequence.append(first_seq[cur_row - 1])
            cur_row -= 1
            cur_col -= 1
        else:
            up = matrix_lcs[cur_row - 1][cur_col]
            left = matrix_lcs[cur_row][cur_col - 1]
            if up > left:
                cur_row -= 1
            else:
                cur_col -= 1
    return result_subsequence[::-1]


def main():
    with open('input.txt', 'r') as file_in:
        n = int(file_in.readline().strip())
        first_seq = tuple(map(int, file_in.readline().strip().split()))
        m = int(file_in.readline().strip())
        second_seq = tuple(map(int, file_in.readline().strip().split()))
    result = longest_common_subsequence(first_seq, second_seq, n, m)
    print(*result, sep=' ')


if __name__ == '__main__':
    main()
