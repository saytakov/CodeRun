def main():
    bricks = {}
    with open('input.txt', 'r') as file_in:
        count_briсks = int(file_in.readline().strip())
        for _ in range(count_briсks):
            width, height = map(int, file_in.readline().strip().split())
            if width not in bricks:
                bricks[width] = height
            else:
                if height > bricks[width]:
                    bricks[width] = height
    print(sum(bricks.values()))


if __name__ == '__main__':
    main()
