import sys


def main():
    with open('input.txt', 'r') as file_in:
        count_requests = int(file_in.readline().strip())
    # count_requests = int(sys.stdin.readline().strip())
        for _ in range(count_requests):
            # a1, a2, a3 = map(int, sys.stdin.readline().strip().split())
            a1, a2, a3 = map(int, file_in.readline().strip().split())
            g1, g2, g3 = a1 % 3, a2 % 3, a3 % 3
            nim = g1 ^ g2 ^ g3
            print(1 if nim != 0 else 0)


if __name__ == '__main__':
    main()
