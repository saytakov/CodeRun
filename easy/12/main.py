# import sys
from collections import deque


def search_path(paths: list[list[int]], start: int, goal: int):
    queue = deque([[start]])
    visited: set = set()

    while queue:
        path: list[int] = queue.popleft()
        node: int = path[-1]

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return len(path) - 1

        for neighbor in paths[node]:
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)

    return None


def main():
    with open('input.txt', 'r') as file_in:
        n = int(file_in.readline())
        # n = int(sys.stdin.readline())
        all_paths = []
        for i in range(n):
            paths = tuple(map(int, file_in.readline().strip().split()))
            # paths = tuple(map(int, sys.stdin.readline().strip().split()))
            roads = [paths[j]*j for j in range(n) if paths[j] != 0]
            all_paths.append(roads)
        start, goal = list(map(int, file_in.readline().strip().split()))
        # start, goal = list(map(int, sys.stdin.readline().strip().split()))

    result = search_path(all_paths, start-1, goal-1)
    print(result)


if __name__ == '__main__':
    main()
