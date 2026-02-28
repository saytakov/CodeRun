from collections import deque
from pprint import pprint


def add_or_create_vertex(vertexs: dict[int, list[int]], start: int, end: int):
    if start in vertexs:
        vertexs[start].append(end)
    else:
        vertexs[start] = [end]


def dfs(vertexs):
    visited = set()
    queue = deque([1])

    while queue:
        cur_vertex = queue.popleft()

        visited.add(cur_vertex)

        if len(visited) == len(vertexs):
            break

        for new_vertex in vertexs[cur_vertex]:
            if new_vertex not in visited:
                queue.appendleft(new_vertex)

    return sorted(visited)


def main():
    vertexs = {1: []}
    with open('input.txt', 'r') as file_in:
        n, m = map(int, file_in.readline().strip().split())
        for _ in range(m):
            start, end = map(int, file_in.readline().strip().split())
            add_or_create_vertex(vertexs, start, end)
            add_or_create_vertex(vertexs, end, start)

    result = dfs(vertexs)
    print(len(result))
    print(*result)


if __name__ == '__main__':
    main()
