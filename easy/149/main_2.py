import heapq


def main():
    result = []
    with open('input.txt', 'r') as file_in:
        count_number = int(file_in.readline().strip())
        arr = list(map(int, file_in.readline().strip().split()))
    heapq.heapify(arr)
    for i in range(count_number):
        result.append(heapq.heappop(arr))


if __name__ == '__main__':
    main()
