import sys
from functools import lru_cache

# easy


@lru_cache(maxsize=None)
def sum_moves(m, n):
    if min(m, n) <= abs(m-n):
        return 0
    if (m == 1) and (n == 1):
        return 1
    return sum_moves(m-2, n-1) + sum_moves(m-1, n-2)


def main():
    m, n = map(int, sys.stdin.readline().split(' '))
    result = sum_moves(m, n)
    print(result)


if __name__ == '__main__':
    main()
