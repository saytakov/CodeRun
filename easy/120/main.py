# def binary_search_tree(numbers):
#     if len(numbers) == 0:
#         return 0
#     start = numbers[0]
#     paths = {numbers[0]: [-1, -1, 1]}
#     max_level = 1
#     for number in numbers:
#         if number in paths:
#             continue
#         cur_paths: list[int] = paths[start]
#         cur_number: int = start
#         while True:
#             if number > cur_number:
#                 if cur_paths[1] == -1:
#                     paths[cur_number][1] = number
#                     paths[number] = [-1, -1, paths[cur_number][2] + 1]
#                     max_level = max(paths[cur_number][2] + 1, max_level)
#                     break
#                 else:
#                     cur_number = cur_paths[1]
#                     cur_paths = paths[cur_number]
#             elif number < cur_number:
#                 if cur_paths[0] == -1:
#                     paths[cur_number][0] = number
#                     paths[number] = [-1, -1, paths[cur_number][2] + 1]
#                     max_level = max(paths[cur_number][2] + 1, max_level)
#                     break
#                 else:
#                     cur_number = cur_paths[0]
#                     cur_paths = paths[cur_number]
#     return max_level

# def binary_search_tree(numbers):
#     intervals = [(0, sys.maxsize, 0)]
#     max_level = 0
#     for number in numbers:
#         left = 0
#         right = len(intervals)
#         while left <= right:
#             mid = (left + right) // 2
#             min_, max_, level = intervals[mid]
#             if min_ < number < max_:
#                 max_level = max(max_level, level + 1)
#                 intervals.remove((min_, max_, level))
#                 if (max_ - number) > 1:
#                     intervals.insert(mid, (number, max_, level + 1))
#                 if (number - min_) > 1:
#                     intervals.insert(mid, (min_, number, level + 1))
#                 break
#             elif number < min_:
#                 right = mid - 1
#             elif number > max_:
#                 left = mid + 1
#             else:
#                 break
#     return max_level


# def main():
#     with open('input.txt', 'r') as file_in:
#         numbers = tuple(map(int, file_in.readline().strip().split()))[:-1]
        
#     result = binary_search_tree(numbers)
#     print(result)


class Tree:
    def __init__(self, key: int):
        self.key: int = key
        self.left: dict[int, Tree] = {}
        self.right: dict[int, Tree] = {}


class TreeRoot(Tree):
    def __init__(self, key: int, depth: int):
        super().__init__(key)
        self.max_depth = depth


def binary_search_tree(tree: TreeRoot | None, value: int, depth: int):
    if not tree:
        tree = TreeRoot(value, depth)
    else:
        current_node = tree
        current_depth = 0

        while True:
            current_depth += 1

            if value < current_node.key:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = Tree(value)
                    tree.max_depth = max(tree.max_depth, current_depth + 1)
                    break
            else:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = Tree(value)
                    tree.max_depth = max(tree.max_depth, current_depth + 1)
                    break
    return tree


def main():
    with open('input.txt', 'r') as file_in:
        numbers = tuple(dict.fromkeys(file_in.readline().strip().split()))
        # numbers = tuple(map(int, file_in.readline().strip().split()))[:-1]

    tree = None
    for value in numbers:
        value = int(value)
        if not value:
            break
        tree = binary_search_tree(tree, value, 1)

    print(tree.max_depth)

    # result = binary_search_tree(numbers)
    # print(result)


if __name__ == '__main__':
    main()
