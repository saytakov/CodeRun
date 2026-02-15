class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class RootNode(Node):
    def __init__(self, key):
        super().__init__(key)
        self.empty = set([key])


def build_tree(root: RootNode, key: int):
    if root is None:
        root = RootNode(key)
        return root
    else:
        cur_node = root

        while True:
            if key < cur_node.key:
                if cur_node.left:
                    cur_node = cur_node.left
                else:
                    cur_node.left = Node(key)
                    root.empty.add(key)
                    root.empty.discard(cur_node.key)
                    return root
            else:
                if cur_node.right:
                    cur_node = cur_node.right
                else:
                    cur_node.right = Node(key)
                    root.empty.add(key)
                    root.empty.discard(cur_node.key)
                    return root


def main():
    with open('input.txt') as file_in:
        numbers = list(dict.fromkeys(map(int, file_in.readline().strip().split())))

    tree = None

    for number in numbers:
        if number == 0:
            break

        tree = build_tree(tree, number)

    if tree:
        print(*sorted(tree.empty), sep='\n')


if __name__ == '__main__':
    main()
