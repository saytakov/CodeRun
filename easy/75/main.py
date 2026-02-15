def min_int(interval: int, count: int):
    return count + (count - 1) * interval


def max_int(interval: int, count: int):
    return count + (count + 1) * interval


def main():
    with open('input.txt', 'r') as file_in:
        interval_a = int(file_in.readline().strip())
        interval_b = int(file_in.readline().strip())
        count_a = int(file_in.readline().strip())
        count_b = int(file_in.readline().strip())
        mn = max(min_int(interval_a, count_a), min_int(interval_b, count_b))
        mx = min(max_int(interval_a, count_a), max_int(interval_b, count_b))
        if mn > mx:
            print(-1)
        else:
            print(mn, mx)


if __name__ == '__main__':
    main()
