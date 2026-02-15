def count_balls(target):
    return 1 * (2 ** target - 1)


def main():
    with open('input.txt', 'r') as file_in:
        k = int(file_in.readline().strip())
    print(count_balls(k))


if __name__ == '__main__':
    main()
