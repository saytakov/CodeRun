class Graph:
    def __init__(self, graph, count_nodes):
        self.count_nodes = count_nodes
        self.graph = [0] + graph

    def _find_source(self):
        inputs = [0 for _ in range(self.count_nodes + 1)]
        for i in range(1, self.count_nodes + 1):
            inputs[self.graph[i]] += 1
        sources = []
        for i in range(1, self.count_nodes + 1):
            if inputs[i] == 0:
                sources.append(i)
        if len(sources) == 1:
            return sources[0]
        else:
            return

    def _search_cycle(self, start):
        visited = set()

        cur_node = start
        visited.add(start)
        while True:
            new_node = self.graph[cur_node]
            if (new_node in visited) and (len(visited) != self.count_nodes):
                return
            elif (new_node in visited) and (len(visited) == self.count_nodes):
                return cur_node
            else:
                visited.add(new_node)
                cur_node = new_node

    def swap_nodes(self):
        source = self._find_source()
        if source is None:
            return -1, -1
        stock = self._search_cycle(source)
        if stock is None:
            return -1, -1
        return stock, source


def main():
    # with open('input.txt', 'r') as file_in:
        # count_vertices = int(file_in.readline().strip())
        # vertices = list(map(int, file_in.readline().strip().split()))
    count_vertices = int(input().strip())
    vertices = list(map(int, input().strip().split()))
    graph = Graph(vertices, count_vertices)
    print(*graph.swap_nodes())


if __name__ == '__main__':
    main()
