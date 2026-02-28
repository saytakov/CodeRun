from collections import deque


class Graph:
    def __init__(self, count_vertices: int, count_lines: int):
        self.count_vertices = count_vertices
        self.count_lines = count_lines
        self.vertices = [[] for _ in range(count_vertices + 1)]
        self.lines = [set() for _ in range(count_lines)]

    def add_line(self, i_line: int, line: tuple[int]):
        self.lines[i_line].update(line)
        for vertex in line:
            self.vertices[vertex].append(i_line)

    def bfs(self, start: int, target: int):
        queue = deque([(level, 0) for level in self.vertices[start]])
        visited = set()

        while queue:
            i_line, count_move = queue.popleft()
            visited.add(i_line)

            if target in self.lines[i_line]:
                return count_move

            for vertex_in_line in list(self.lines[i_line]):
                for line_vertex in self.vertices[vertex_in_line]:
                    if line_vertex not in visited:
                        queue.append((line_vertex, count_move + 1))
        return -1


def main():
    with open('input.txt', 'r') as file_in:
        count_vertices = int(file_in.readline().strip())
        count_lines = int(file_in.readline().strip())
        graph = Graph(count_vertices, count_lines)
        for i_line in range(count_lines):
            line = tuple(map(int, file_in.readline().strip().split()))
            graph.add_line(i_line, line[1:])
        start, target = map(int, file_in.readline().strip().split())
    result = graph.bfs(start, target)
    print(result)


if __name__ == '__main__':
    main()
