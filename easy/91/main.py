def count_cars_with_target(cars: list[int], count_cars: int, target: int):
    result = 0
    left = 0
    right = 0
    cur_summ = cars[0]

    while True:
        if cur_summ >= target:
            if cur_summ == target:
                result += 1
            cur_summ -= cars[left]
            left += 1
        else:
            if right + 1 < count_cars:
                right += 1
                cur_summ += cars[right]
            else:
                break
    return result


def main():
    with open('input.txt', 'r') as file_in:
        count_cars, target = map(int, file_in.readline().strip().split())
        cars = list(map(int, file_in.readline().strip().split()))
    result = count_cars_with_target(cars, count_cars, target)
    print(result)


if __name__ == '__main__':
    main()
