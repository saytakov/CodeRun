# from sys import setrecursionlimit

# setrecursionlimit(10**6)


# class Graph:
#     def __init__(self, count_vertices: int):
#         self.count_vertices: int = count_vertices
#         self.graph = [[] for _ in range(count_vertices + 1)]
#         self.error = 0
#         self.stack = []
#         self.visited = [False] * (self.count_vertices + 1)
#         self.path = []

#     def add_edge(self, start: int, end: int):
#         self.graph[start].append(end)

#     def topological_sort_util(self, v: int):
#         self.visited[v] = True
#         if self.error:
#             return
#         for i in self.graph[v]:
#             if not self.visited[i]:
#                 self.path.append(i)
#                 self.topological_sort_util(i)
#                 self.path.pop()
#             elif self.visited[i] and i in self.path:
#                 self.error = 1
#         self.stack.append(v)

#     def topological_sort(self):
#         for i in range(1, self.count_vertices + 1):
#             if not self.visited[i]:
#                 self.path.append(i)
#                 self.topological_sort_util(i)
#                 self.path.pop()
#                 if self.error:
#                     return [-1]
#         return self.stack[::-1]


# def main():
#     with open('input.txt', 'r') as file_in:
#         n, m = map(int, file_in.readline().strip().split())
#         graph = Graph(n)
#         for _ in range(m):
#             start, end = map(int, file_in.readline().strip().split())
#             graph.add_edge(start, end)
#     result = graph.topological_sort()
#     print(*result)


# if __name__ == '__main__':
#     main()


# class Graph:
#     def __init__(self, count_vertices: int):
#         self.count_vertices: int = count_vertices
#         self.graph = [[] for _ in range(count_vertices + 1)]
#         self.error = 0

#     def add_edge(self, start: int, end: int):
#         self.graph[start].append(end)

#     def topological_sort_util(self, v, status, result: list[int]):
#         path = [v]

#         while path:
#             if self.error:
#                 return

#             cur_vertex = path[-1]

#             if status[cur_vertex] == 0:
#                 status[cur_vertex] = 1

#             count_moves = 0
#             for new_vertex in self.graph[cur_vertex]:
#                 if not status[new_vertex]:
#                     path.append(new_vertex)
#                     count_moves += 1
#                     break
#                 elif (new_vertex in path):
#                     self.error = 1

#             if count_moves == 0:
#                 status[cur_vertex] = 2
#                 result.insert(0, cur_vertex)
#                 path.pop()
#         return

#     def topological_sort(self):
#         status = [0] * (self.count_vertices + 1)
#         result = []

#         for i in range(1, self.count_vertices + 1):
#             if self.error:
#                 return [-1]
#             if not status[i]:
#                 self.topological_sort_util(i, status, result)
#         return result


# def main():
#     with open('input.txt', 'r') as file_in:
#         n, m = map(int, file_in.readline().strip().split())
#         graph = Graph(n)
#         for _ in range(m):
#             start, end = map(int, file_in.readline().strip().split())
#             graph.add_edge(start, end)
#     result = graph.topological_sort()
#     print(*result)


# if __name__ == '__main__':
#     main()


from collections import deque


class Graph:
    def __init__(self, count_vertices: int):
        self.count_vertices: int = count_vertices
        self.graph = [[] for _ in range(count_vertices + 1)]
        self.error = 0

    def add_edge(self, start: int, end: int):
        self.graph[start].append(end)

    def khan_topological_sort(self):
        in_degree = [0] * (self.count_vertices + 1)
        for vertex in range(1, self.count_vertices + 1):
            for new_vertex in self.graph[vertex]:
                in_degree[new_vertex] += 1

        queue = deque()
        for i in range(1, self.count_vertices + 1):
            if in_degree[i] == 0:
                queue.append(i)

        result = []
        while queue:
            cur_vertex = queue.popleft()
            result.append(cur_vertex)

            for new_vertex in self.graph[cur_vertex]:
                in_degree[new_vertex] -= 1
                if in_degree[new_vertex] == 0:
                    queue.append(new_vertex)

        if len(result) != self.count_vertices:
            return [-1]
        return result


def main():
    with open('input.txt', 'r') as file_in:
        n, m = map(int, file_in.readline().strip().split())
        graph = Graph(n)
        for _ in range(m):
            start, end = map(int, file_in.readline().strip().split())
            graph.add_edge(start, end)
    result = graph.khan_topological_sort()
    print(*result)


if __name__ == '__main__':
    main()
