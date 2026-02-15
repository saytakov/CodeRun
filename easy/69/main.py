def more_neighbors(numbers):
    count = 0
    for i in range(1, len(numbers) - 1):
        if numbers[i] > numbers[i-1] and numbers[i] > numbers[i+1]:
            count += 1
    return count


def main():
    with open('input.txt', 'r') as file_in:
        numbers = list(map(int, file_in.readline().strip().split()))
    result = more_neighbors(numbers)
    print(result)


if __name__ == '__main__':
    main()
