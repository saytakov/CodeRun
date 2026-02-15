def heapfy(arr, n, i):
    largest = i
    right = (i * 2) + 1
    r = (i * 2) + 2

    if right < n and arr[largest] < arr[right]:
        largest = right

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapfy(arr, n, largest)


def heap_sort(arr: list[int]) -> None:
    n = len(arr)

    for i in range(n-1, -1, -1):
        heapfy(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapfy(arr, i, 0)


def main():
    with open('input.txt', 'r') as file_in:
        count_numbers = int(file_in.readline().strip())
        arr = list(map(lambda x: int(x), file_in.readline().strip().split()))
    heap_sort(arr)
    print(*arr)


if __name__ == '__main__':
    main()
