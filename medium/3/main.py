from pprint import pprint


def find_longest_path(matrix: tuple[tuple[int, ...], ...], rows: int, cols: int) -> list[int, str]:
    result_matrix = [[[0, ''] for _ in range(cols)] for _ in range(rows)]
    result_matrix[0][0][0] = matrix[0][0]
    for col in range(1, cols):
        prev_wiegth = result_matrix[0][col - 1][0]
        prev_path = result_matrix[0][col - 1][1]
        result_matrix[0][col] = [prev_wiegth + matrix[0][col], prev_path + 'R ']
    for row in range(1, rows):
        prev_wiegth = result_matrix[row - 1][0][0]
        prev_path = result_matrix[row - 1][0][1]
        result_matrix[row][0] = [prev_wiegth + matrix[row][0], prev_path + 'D ']
    for row in range(1, rows):
        for col in range(1, cols):
            up = result_matrix[row - 1][col]
            left = result_matrix[row][col - 1]
            cur_weigth = matrix[row][col]
            if up[0] > left[0]:
                new_cell = [cur_weigth + up[0], up[1] + 'D ']
            else:
                new_cell = [cur_weigth + left[0], left[1] + 'R ']
            result_matrix[row][col] = new_cell
    return result_matrix[-1][-1]


def main():
    with open('input.txt', 'r') as file_in:
        n, m = map(int, file_in.readline().strip().split())
        matrix = tuple(tuple(map(int, file_in.readline().strip().split())) for _ in range(n))
    result = find_longest_path(matrix, n, m)
    print(*result, sep='\n')


if __name__ == '__main__':
    main()
