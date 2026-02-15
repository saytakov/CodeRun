def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)


def main():
    types = set()
    with open('input.txt', 'r') as file_in:
        count = int(file_in.readline().strip())
        for _ in range(count):
            a, b, c = sorted(map(int, file_in.readline().strip().split()))
            common_divisor = gcd(a, gcd(c, b))
            types.add(
                (a // common_divisor, b // common_divisor, c // common_divisor)
            )
    print(len(types))


if __name__ == '__main__':
    main()
