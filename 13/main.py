from collections import deque


class Graph:
    def __init__(self, count_vertices):
        self.count_vertices = count_vertices
        self.graph = [[] for _ in range(count_vertices + 1)]
        self.min_path = []

    def add_edge(self, start, end):
        self.graph[start].append(end)
        self.graph[end].append(start)

    def bfs(self, start, end):
        queue = deque([[start]])
        visited = set()

        while queue:
            cur_path = queue.popleft()
            cur_vertex = cur_path[-1]
            visited.add(cur_vertex)

            if cur_vertex == end:
                return cur_path

            for new_vertex in self.graph[cur_vertex]:
                if new_vertex not in visited:
                    new_path = list(cur_path)
                    new_path.append(new_vertex)
                    queue.append(new_path)

        return [-1]


def main():
    with open('input.txt', 'r') as file_in:
        count_vertices = int(file_in.readline().strip())
        graph = Graph(count_vertices)
        for row_i in range(count_vertices):
            row = list(map(int, file_in.readline().strip().split()))
            for col_i in range(row_i, count_vertices):
                if row[col_i] == 1:
                    graph.add_edge(row_i + 1, col_i + 1)
        start, end = map(int, file_in.readline().strip().split())
    result = graph.bfs(start, end)
    if len(result) == 1:
        if result[0] == -1:
            print(-1)
        else:
            print(0)
    else:
        print(len(result) - 1)
        print(*result)


if __name__ == '__main__':
    main()
