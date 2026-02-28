def main():
    with open('input.txt', 'r') as file_in:
        n, t = map(int, file_in.readline().strip().split())
        floors = list(map(int, file_in.readline().strip().split()))
        target = int(file_in.readline().strip())
    # n, t = map(int, input().strip().split())
    # floors = list(map(int, input().strip().split()))
    # target = int(input().strip())
    result = float('inf')
    target_i = target - 1
    for i in range(n):
        left = floors[i] - floors[0]
        right = floors[-1] - floors[i]
        if left <= right:
            if target_i < i:
                if i - target_i > t:
                    continue
            elif target_i > i:
                if (left * 2 + floors[target_i] - floors[i]) > t:
                    continue
            result = min(result, left * 2 + right)
        else:
            if target_i < i:
                if (right * 2 + floors[i] - floors[target_i]) > t:
                    continue
            elif target_i > i:
                if (floors[target_i] - floors[i]) > t:
                    continue
            result = min(result, right * 2 + left)
    print(result)


if __name__ == '__main__':
    main()
