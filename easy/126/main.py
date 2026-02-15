class NodeTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class RootTree(NodeTree):
    def __init__(self, key):
        super().__init__(key)
        self.one = set()


def binary_tree(root: RootTree, key: int):
    if root is None:
        root = RootTree(key)
        return root
    else:
        cur_node = root

        while True:
            if key < cur_node.key:
                if cur_node.left:
                    cur_node = cur_node.left
                else:
                    cur_node.left = NodeTree(key)
                    if cur_node.left and not cur_node.right:
                        root.one.add(cur_node.key)
                    else:
                        root.one.discard(cur_node.key)
                    return root
            else:
                if cur_node.right:
                    cur_node = cur_node.right
                else:
                    cur_node.right = NodeTree(key)
                    if cur_node.right and not cur_node.left:
                        root.one.add(cur_node.key)
                    else:
                        root.one.discard(cur_node.key)
                    return root


def main():
    with open('input.txt', 'r') as file_in:
        numbers = list(dict.fromkeys(map(int, file_in.readline().strip().split())))

    tree = None

    for number in numbers:
        if number == 0:
            break

        tree = binary_tree(tree, number)

    if tree:
        print(*sorted(tree.one), sep='\n')


if __name__ == '__main__':
    main()
