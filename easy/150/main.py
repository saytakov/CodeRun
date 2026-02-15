def three_ones(target):
    data = [(1, 1) for _ in range(target + 1)]

    for i in range(1, target + 1):
        if i < 3:
            count_0 = data[i-1][0]
            count = count_0 * 2
        else:
            count_0 = data[i-1][0]
            count = 2 * count_0 - data[i-3][1]
        data[i] = (count, count_0)
    return data[-1][0]


def main():
    with open('input.txt', 'r') as file_in:
        target = int(file_in.readline().strip())
    print(three_ones(target))


if __name__ == '__main__':
    main()
