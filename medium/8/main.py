def dfs(start: int, vertexs: dict[int, list[int]]):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()

        visited.add(vertex)

        for new_vertex in vertexs[vertex]:
            if new_vertex not in visited:
                stack.append(new_vertex)

    return visited


def main():
    with open('input.txt', 'r') as file_in:
        n, m = map(int, file_in.readline().strip().split())
        vertexs = {i: [] for i in range(1, n + 1)}
        for _ in range(m):
            start, end = map(int, file_in.readline().strip().split())
            vertexs[start].append(end)
            vertexs[end].append(start)
    all_visited = set()
    components = []
    count_components = 0
    for vertex in vertexs:
        if vertex not in all_visited:
            count_components += 1
            result = dfs(vertex, vertexs)
            components.append(result)
            all_visited |= result

    print(count_components)
    for component in components:
        print(len(component))
        print(*component)


if __name__ == '__main__':
    main()
