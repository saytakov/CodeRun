def search_target(sequence: list[int], targets: list[int], count_sequence: int, count_targets: int):
    for target in targets:
        left = 0
        right = count_sequence - 1
        while True:
            i_cur_value = (right + left) // 2
            if (left == right) and (sequence[i_cur_value] != target):
                print('NO')
                break
            if sequence[i_cur_value] == target:
                print('YES')
                break
            elif sequence[i_cur_value] > target:
                right = i_cur_value
            else:
                left = i_cur_value + 1


def main():
    with open('input.txt', 'r') as file_in:
        n, k = map(int, file_in.readline().strip().split())
        in_search = list(map(int, file_in.readline().strip().split()))
        targets = list(map(int, file_in.readline().strip().split()))
    search_target(in_search, targets, n, k)


if __name__ == '__main__':
    main()
