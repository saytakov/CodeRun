def main():
    columns = set()
    with open('input.txt', 'r') as file_in:
        count_birds = int(file_in.readline())
        for _ in range(count_birds):
            columns.add(file_in.readline().strip().split()[0])
    print(len(columns))


if __name__ == '__main__':
    main()
