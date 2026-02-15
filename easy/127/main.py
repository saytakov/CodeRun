class NodeTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# class RootTree(NodeTree):
#     def __init__(self, key):
#         super().__init__(key)
#         self.depths = {key: 1}


def binary_tree(root: NodeTree, key):
    if root is None:
        root = NodeTree(key)
        return root
    else:
        cur_node = root

        while True:
            if key < cur_node.key:
                if cur_node.left:
                    cur_node = cur_node.left
                else:
                    cur_node.left = NodeTree(key)
                    return root
            else:
                if cur_node.right:
                    cur_node = cur_node.right
                else:
                    cur_node.right = NodeTree(key)
                    return root


def dfs(node: NodeTree):
    if node is None:
        return 0, True

    depth_left, status_left = dfs(node.left)
    depth_right, status_right = dfs(node.right)

    if abs(depth_left - depth_right) > 1:
        status = False
    else:
        status = status_right and status_left
    return max(depth_right, depth_left) + 1, status


def main():
    with open('input.txt', 'r') as file_in:
        numbers = list(dict.fromkeys(map(int, file_in.readline().strip().split())))

    tree = None

    for number in numbers:
        if number == 0:
            break
        tree = binary_tree(tree, number)

    depth, status = dfs(tree)

    if status:
        print('YES')
    else:
        print('NO')

    # if tree:
    #     depths = sorted(tree.depths.values())
    #     for i in range(len(depths) - 1):
    #         if depths[i + 1] - depths[i] > 1:
    #             print('NO')
    #             return
    #     print('YES')
    # else:
    #     print('NO')


if __name__ == '__main__':
    main()
