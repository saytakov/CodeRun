def fibonacci_numbers(length_table, max_jump):
    table = [0 for _ in range(length_table)]
    for i in range(length_table):
        if i <= max_jump:
            for j in range(1, i):
                table[i] += table[j]
            table[i] += 1
        else:
            for j in range(i-max_jump, i):
                table[i] += table[j]
    return table[-1]


def main():
    with open('input.txt', 'r') as file_in:
        n, k = map(int, file_in.readline().strip().split())
    print(fibonacci_numbers(n, k))


if __name__ == '__main__':
    main()
