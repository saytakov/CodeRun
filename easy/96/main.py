def search_max_subsequence(sequence, len_sequence, max_count):
    left = 0
    right = 0
    max_length = -1
    first_i = -1
    cur_length = 0
    count_letter = {}
    while right < len_sequence and left <= right:
        if sequence[right] in count_letter:
            if count_letter[sequence[right]] + 1 > max_count:
                count_letter[sequence[right]] += 1
                cur_length += 1
                while count_letter[sequence[right]] > max_count:
                    count_letter[sequence[left]] -= 1
                    cur_length -= 1
                    left += 1
                right += 1
            else:
                count_letter[sequence[right]] += 1
                cur_length += 1
                right += 1
        else:
            count_letter[sequence[right]] = 1
            right += 1
            cur_length += 1
        if max_length < cur_length:
            max_length = cur_length
            first_i = left + 1
    return max_length, first_i


def main():
    with open('input.txt', 'r') as file_in:
        len_sequence, max_count = map(int, file_in.readline().strip().split())
        sequence = file_in.readline().strip()
    result = search_max_subsequence(sequence, len_sequence, max_count)
    print(' '.join(map(str, result)))


if __name__ == '__main__':
    main()
