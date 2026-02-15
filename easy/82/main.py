def temperature(start: int, target: int, mode: str):
    if (start < target) and (mode in ('heat', 'auto')):
        return target
    elif (start > target) and (mode in ('freeze', 'auto')):
        return target
    else:
        return start


def main():
    with open('input.txt', 'r') as file_in:
        start, target = map(int, file_in.readline().strip().split())
        mode = file_in.readline().strip()
    result = temperature(start, target, mode)
    print(result)


if __name__ == '__main__':
    main()
