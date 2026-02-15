def main():
    result = 0
    with open('input.txt', 'r') as file_in:
        count_letters = int(file_in.readline().strip())
        prev = None
        for _ in range(count_letters):
            cur = int(file_in.readline().strip())

            if prev is None:
                prev = cur
                continue

            result += min(prev, cur)
            prev = cur
    print(result)


if __name__ == '__main__':
    main()
