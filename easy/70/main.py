def search_near(numbers, target):
    result = 0
    diff = 2001
    for number in numbers:
        if number == target:
            return number
        cur_diff = abs(target - number)
        if diff > cur_diff:
            diff = cur_diff
            result = number
    return result


def main():
    with open('input.txt', 'r') as file_in:
        count_numbers = int(file_in.readline().strip())
        numbers = map(int, file_in.readline().strip().split())
        target = int(file_in.readline().strip())
    result = search_near(numbers, target)
    print(result)


if __name__ == '__main__':
    main()
