def search_max_subsequence(sequence: list[int], count_numbers: int):
    prev = [-1] * count_numbers
    len_paths = [1] * count_numbers
    for i in range(1, count_numbers):
        for j in range(i):
            if sequence[i] > sequence[j] and len_paths[j] + 1 > len_paths[i]:
                len_paths[i] = len_paths[j] + 1
                prev[i] = j

    max_path = len_paths.index(max(len_paths))

    result = []

    while max_path != -1:
        result.append(sequence[max_path])
        max_path = prev[max_path]

    return result[::-1]


def main():
    with open('input.txt', 'r') as file_in:
        count_numbers = int(file_in.readline().strip())
        sequence = list(map(int, file_in.readline().strip().split()))

    result = search_max_subsequence(sequence, count_numbers)

    res_for_print = ' '.join(map(str, result))

    print(res_for_print)


if __name__ == '__main__':
    main()
