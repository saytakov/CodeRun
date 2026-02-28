class Graph:
    def __init__(self, count_vertices):
        self.count_vertices = count_vertices
        self.graph = [[] for _ in range(count_vertices + 1)]
        self.visited = [False for _ in range(count_vertices + 1)]

    def add_edge(self, start, end):
        self.graph[start].append(end)
        self.graph[end].append(start)

    def from_matrix_to_graph(self, matrix):
        for row in range(self.count_vertices):
            for col in range(row, self.count_vertices):
                if matrix[row][col] == 1:
                    self.add_edge(row + 1, col + 1)

    def _dfs(self, start):
        stack = [[start]]

        while stack:
            cur_path = stack.pop()
            cur_vertex = cur_path[-1]
            prev_vertex = cur_path[-2] if len(cur_path) > 1 else None
            self.visited[cur_vertex] = True

            for new_vertex in self.graph[cur_vertex]:
                if not self.visited[new_vertex]:
                    new_path = list(cur_path)
                    new_path.append(new_vertex)
                    stack.append(new_path)
                elif (new_vertex in cur_path) and (new_vertex != prev_vertex):
                    start = cur_path.index(new_vertex)
                    return cur_path[start:]
        return

    def found_cycle(self):
        for i in range(1, self.count_vertices + 1):
            if not self.visited[i]:
                if result := self._dfs(i):
                    return result
        return


def main():
    with open('input.txt', 'r') as file_in:
        count_vertices = int(file_in.readline())
        matrix = []
        for _ in range(count_vertices):
            matrix.append(list(map(int, file_in.readline().strip().split())))
    graph = Graph(count_vertices)
    graph.from_matrix_to_graph(matrix)
    if (result := graph.found_cycle()) is None:
        print('NO')
    else:
        print('YES')
        print(len(result))
        print(*result)


if __name__ == '__main__':
    main()
