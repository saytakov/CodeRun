def search_median(sequences, count_sequence, length_sequence):
    for i in range(len(sequences)):
        for j in range(i + 1, len(sequences)):
            cur_value = 0
            cur_first_i = 0
            cur_second_i = 0
            cur_length = 0
            while cur_length < length_sequence:                    
                first_value = sequences[i][cur_first_i]
                second_value = sequences[j][cur_second_i]
                if first_value <= second_value:
                    cur_first_i += 1
                    cur_value = first_value
                else:
                    cur_second_i += 1
                    cur_value = second_value
                cur_length += 1
            print(cur_value)


def main():
    with open('input.txt', 'r') as file_in:
        count_sequence, length_sequence = map(int, file_in.readline().strip().split())
        sequences = [[] for _ in range(count_sequence)]
        for i in range(count_sequence):
            sequences[i] = list(map(int, file_in.readline().strip().split()))
    search_median(sequences, count_sequence, length_sequence)


if __name__ == '__main__':
    main()
