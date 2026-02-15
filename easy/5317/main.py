import sys


def add_or_create_path(
    paths: dict[int, list[int]],
    key: int,
    value: int
) -> None:
    if key in paths:
        paths[key].append(value)
    else:
        paths[key] = [value]


def dfs(
    start: int,
    visitors: set[int],
    towns: dict[int, list[int]],
) -> int:

    count_paths = 0
    visitors.add(start)

    for town in towns[start]:
        if town not in visitors:
            count_paths += 1
            count_paths += dfs(town, visitors, towns)

    return count_paths


def main():
    towns: dict[int, list[int]] = {}
    n, m = map(int, sys.stdin.readline().strip().split())
    for _ in range(m):
        start, end = map(int, sys.stdin.readline().strip().split())
        add_or_create_path(towns, start, end)
        add_or_create_path(towns, end, start)
    visitors = set()
    count_paths = 0
    for town in towns:
        if town not in visitors:
            count_paths += dfs(town, visitors, towns)
    print(m - count_paths)


if __name__ == '__main__':
    main()

# def main():
#     towns: dict[int, list[int]] = {}
#     with open('input.txt', 'r') as file_in:
#         n, m = map(int, file_in.readline().strip().split())
#         for _ in range(m):
#             start, end = map(int, file_in.readline().strip().split())
#             add_or_create_path(towns, start, end)
#             add_or_create_path(towns, end, start)
#     visitors = set()
#     count_paths = 0
#     for town in towns:
#         if town not in visitors:
#             count_paths += dfs(town, visitors, towns)
#     print(m - count_paths)