from collections import deque

START = 1


def search_dfs(edges) -> list[int]:
    visited = set()
    queue = deque([START])

    while queue:
        vertex = queue.popleft()

        if vertex in visited:
            continue

        visited.add(vertex)

        if vertex not in edges:
            continue

        for child in edges[vertex]:
            queue.appendleft(child)

    return sorted(visited)


def main():
    with open('input.txt', 'r') as file_in:
        count_vertexs, count_edges = map(
            int, file_in.readline().strip().split()
        )
        edges: dict[int, list[int]] = {}
        for _ in range(count_edges):
            start, end = map(int, file_in.readline().strip().split())
            if end not in edges:
                edges[end] = [start]
            else:
                edges[end].append(start)

        result = search_dfs(edges)
        print(' '.join(map(str, result)))


if __name__ == '__main__':
    main()
