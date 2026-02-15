def lev_distance(str1: str, str2: str) -> int:
    n, m = len(str1), len(str2)
    if n > m:
        n, m = m, n
        str1, str2 = str2, str1

    current = range(m+1)

    for i in range(1, m+1):
        prev, current = current, [i] + [0] * n
        for j in range(1, n+1):
            add, delete, change = prev[j] + 1, current[j-1] + 1, prev[j-1]
            if str1[j-1] != str2[i-1]:
                change += 1
            current[j] = min(add, delete, change)
    return current[-1]

    # table = [[0 for _ in range(m+1)] for _ in range(n+1)]

    # for i in range(1, n+1):
    #     table[i][0] = i
    # for i in range(1, m+1):
    #     table[0][i] = i

    # for i in range(1, n+1):
    #     for j in range(1, m+1):
    #         if str1[i-1] == str2[j-1]:
    #             table[i][j] = table[i-1][j-1]
    #         else:
    #             table[i][j] = min(
    #                 table[i-1][j] + 1, table[i-1][j-1] + 1, table[i][j-1] + 1
    #             )

    # return table[-1][-1]


def main():
    with open('input.txt', 'r') as file_in:
        start = file_in.readline().strip()
        goal = file_in.readline().strip()
    # start = sys.stdin.readline().strip()
    # goal = sys.stdin.readline().strip()

    result = lev_distance(start, goal)

    print(result)


if __name__ == '__main__':
    main()
