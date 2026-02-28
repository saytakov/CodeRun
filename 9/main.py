def dfs(paths, n, m):
    visited = [False for _ in range(n + 1)]
    colors = [0 for _ in range(n + 1)]
    for vertex in range(1, n + 1):
        if not visited[vertex]:
            stack = [[vertex]]
            colors[vertex] = 1
        else:
            continue
        while stack:
            cur_path = stack.pop()
            cur_vertex = cur_path[-1]
            prev_vertex = cur_path[-2] if len(cur_path) > 1 else None
            if prev_vertex:
                colors[cur_vertex] = 3 - colors[prev_vertex]
            visited[cur_vertex] = True

            for new_vertex in paths[cur_vertex]:
                if not visited[new_vertex]:
                    new_path = list(cur_path)
                    new_path.append(new_vertex)
                    stack.append(new_path)
                else:
                    if colors[cur_vertex] == colors[new_vertex]:
                        return False
    return True


def main():
    with open('input.txt', 'r') as file_in:
        n, m = map(int, file_in.readline().strip().split())
        paths = [[] for _ in range(n + 1)]
        for _ in range(m):
            start, end = map(int, file_in.readline().strip().split())
            paths[start].append(end)
            paths[end].append(start)
        if dfs(paths, n, m):
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()

# def dfs(paths, n, m):
#     visited = [False for _ in range(n + 1)]
#     for vertex in range(1, n + 1):
#         if not visited[vertex]:
#             stack = [[vertex]]
#         else:
#             continue
#         while stack:
#             cur_path = stack.pop()
#             cur_vertex = cur_path[-1]
#             prev_vertex = cur_path[-2] if len(cur_path) > 1 else None
#             visited[cur_vertex] = True

#             for new_vertex in paths[cur_vertex]:
#                 if not visited[new_vertex]:
#                     new_path = list(cur_path)
#                     new_path.append(new_vertex)
#                     stack.append(new_path)
#                 else:
#                     if new_vertex == prev_vertex:
#                         continue
#                     elif new_vertex in cur_path:
#                         if (cur_path.index(new_vertex) % 2) == ((len(cur_path) - 1) % 2):
#                             return False
#     return True