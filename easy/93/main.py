def search_count_monuments(monuments, count_monuments, distance):
    left = 0
    right = 1
    result = 0
    while right < count_monuments:
        if left == right:
            right += 1
            continue
        diff = monuments[right] - monuments[left]
        if diff <= distance:
            right += 1
        else:
            result += count_monuments - right
            left += 1
    return result


def main():
    with open('input.txt', 'r') as file_in:
        count_monuments, distance = map(int, file_in.readline().strip().split())
        monuments = list(map(int, file_in.readline().strip().split()))
    result = search_count_monuments(monuments, count_monuments, distance)
    print(result)


if __name__ == '__main__':
    main()
