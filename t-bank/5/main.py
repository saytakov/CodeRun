def main():
    # with open('input.txt', 'r') as file_in:
        # start, end = file_in.readline().strip().split()
    start, end = input().strip().split()

    length_start = len(start)
    length_end = len(end)

    count = 0
    for i in range(length_start, length_end + 1):
        multiple = int('1' * i)
        for i in range(1, 10):
            if (i * multiple) < int(start):
                continue
            elif (i * multiple) > int(end):
                break
            else:
                count += 1
    print(count)


if __name__ == '__main__':
    main()
