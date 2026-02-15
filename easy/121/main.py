class Node:
    def __init__(self, key, depth):
        self.key = key
        self.depth = depth
        self.left = None
        self.right = None


def search_depth(root: Node | None, key: int):
    if root is None:
        root = Node(key, 1)
        return root, 1
    else:
        current_tree = root
        current_depth = root.depth

        while True:
            if key < current_tree.key:
                if current_tree.left:
                    current_tree = current_tree.left
                    current_depth = current_depth + 1
                else:
                    current_tree.left = Node(key, current_depth + 1)
                    return root, current_depth + 1
            else:
                if current_tree.right:
                    current_tree = current_tree.right
                    current_depth = current_depth + 1
                else:
                    current_tree.right = Node(key, current_depth + 1)
                    return root, current_depth + 1


def main():
    with open('input.txt', 'r') as file_in:
        numbers = list(dict.fromkeys(file_in.readline().strip().split()))[:-1]

    tree = None
    answer = []

    for number in numbers:
        number = int(number)
        if number == 0:
            break
        tree, result = search_depth(tree, number)
        answer.append(result)

    print(' '.join(map(str, answer)))


if __name__ == '__main__':
    main()
