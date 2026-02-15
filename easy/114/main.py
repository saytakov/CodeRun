VALUE_TIME = 60*24
# VALUE_TIME = 10


def scanline(sequences, target):
    times = [0 for _ in range(VALUE_TIME)]
    for start, stop in sequences:
        if start == stop:
            target -= 1
            continue
        if stop < start:
            stop = VALUE_TIME + stop
        for i in range(start, stop):
            times[i % (VALUE_TIME)] += 1
    return times.count(target)


def main():
    with open('input.txt', 'r') as file_in:
        count_kassa = int(file_in.readline().strip())
        times_kassa = []
        for _ in range(count_kassa):
            time = list(map(int, file_in.readline().strip().split()))
            open_h = time[0] * 60
            open_m = time[1]
            close_h = time[2] * 60
            close_m = time[3]
            times_kassa.append((open_h + open_m, close_h + close_m))
    result = scanline(times_kassa, count_kassa)
    print(result)


if __name__ == '__main__':
    main()


# 3
# 0 1 0 6
# 0 2 0 2
# 0 7 0 5