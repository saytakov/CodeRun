def max_length_wire(wires, count_wires, target_count):
    left = 1
    right = max(wires)
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        current_count = 0
        for wire in wires:
            current_count += wire // mid
        if current_count >= target_count:
            if mid > answer:
                answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer


def main():
    with open('input.txt', 'r') as file_in:
        n, k = map(int, file_in.readline().strip().split())
        wires = []
        for _ in range(n):
            wires.append(int(file_in.readline().strip()))
    result = max_length_wire(wires, n, k)
    print(result)


if __name__ == '__main__':
    main()
