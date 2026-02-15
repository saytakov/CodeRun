def valid_triangle(sides: list[int]) -> str:
    if sum(sides) - max(sides) > max(sides):
        return 'YES'
    else:
        return 'NO'


def main():
    sides = []
    with open('input.txt', 'r') as file_in:
        for _ in range(3):
            sides.append(int(file_in.readline().strip()))
    print(valid_triangle(sides))


if __name__ == '__main__':
    main()
