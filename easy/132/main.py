def count_buy_stikers(stikers, min_buyers, count_buyer):
    new_stikers = sorted(stikers)
    result = []
    if len(new_stikers) == 0:
        return [0] * count_buyer
    if count_buyer == 0:
        return result
    for target in min_buyers:
        left = 0
        right = len(new_stikers) - 1
        cur_mid = -1

        while left <= right:
            mid = (left + right) // 2
            cur_mid = mid

            if target == new_stikers[mid]:
                break
            elif target < new_stikers[mid]:
                right = mid - 1
            else:
                left = mid + 1
        if target > new_stikers[cur_mid]:
            cur_mid += 1
        result.append(cur_mid)
    return result


def main():
    with open('input.txt', 'r') as file_in:
        count_stikers = int(file_in.readline().strip())
        stikers = list(dict.fromkeys(map(int, file_in.readline().strip().split())))
        count_buyer = int(file_in.readline().strip())
        min_buyers = list(map(int, file_in.readline().strip().split()))
    result = count_buy_stikers(stikers, min_buyers, count_buyer)
    print(*result, sep='\n')


if __name__ == '__main__':
    main()
