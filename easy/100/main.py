def search_nearest(sequence, targets, length_sequence, count_targets):
    for target in targets:
        left = 0
        right = length_sequence - 1
        left_nearest = 10000000000000000000000
        right_nearest = 10000000000000000000000000000
        while True:
            i_cur_value = (left + right) // 2
            if sequence[i_cur_value] == target:
                print(target)
                break
            if sequence[i_cur_value] > target:
                right = i_cur_value
            elif sequence[i_cur_value] < target:
                left = i_cur_value + 1
            if (left == right) and (sequence[i_cur_value] != target):
                if (sequence[i_cur_value] > target):
                    if i_cur_value - 1 > -1:
                        left_nearest = sequence[i_cur_value - 1]
                    else:
                        print(sequence[i_cur_value])
                        break
                    diff_left = abs(target - left_nearest)
                    diff_right = abs(target - sequence[i_cur_value])
                    if diff_left == diff_right:
                        print(min(left_nearest, sequence[i_cur_value]))
                    else:
                        if diff_left < diff_right:
                            print(left_nearest)
                        else:
                            print(sequence[i_cur_value])
                    break
                else:
                    if i_cur_value + 1 < length_sequence:
                        right_nearest = sequence[i_cur_value + 1]
                    else:
                        print(sequence[i_cur_value])
                        break
                    diff_left = abs(target - sequence[i_cur_value])
                    diff_right = abs(target - sequence[i_cur_value + 1])
                    if diff_left == diff_right:
                        print(min(left_nearest, sequence[i_cur_value]))
                    else:
                        if diff_left < diff_right:
                            print(sequence[i_cur_value])
                        else:
                            print(right_nearest)
                    break


def main():
    with open('input.txt', 'r') as file_in:
        n, k = map(int, file_in.readline().strip().split())
        sequence = list(map(int, file_in.readline().strip().split()))
        targets = map(int, file_in.readline().strip().split())
    search_nearest(sequence, targets, n, k)


if __name__ == '__main__':
    main()
