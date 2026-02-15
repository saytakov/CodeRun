def main():
    min_x = 1_000_000_001
    min_y = 1_000_000_001
    max_x = 0
    max_y = 0
    with open('input.txt', 'r') as file_in:
        count_points = int(file_in.readline().strip())
        for _ in range(count_points):
            x, y = map(int, file_in.readline().strip().split())
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
    print(min_x, min_y, max_x, max_y)


if __name__ == '__main__':
    main()
