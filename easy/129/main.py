from collections import deque


def dfs(parent_child, parent):
    result: set[tuple[str, int]] = set()

    queue = deque([[parent]])

    while queue:
        cur_queue = queue.popleft()
        cur_child = cur_queue[-1]

        if cur_child in parent_child:
            for child in parent_child[cur_child]:
                new_queue = cur_queue.copy()
                new_queue.append(child)
                result.add((cur_child, len(cur_queue) - 1))
                queue.appendleft(new_queue)
        else:
            result.add((cur_child, len(cur_queue) - 1))

    return result


def main():
    parent_child: dict[str, list[str]] = {}
    childs = set()
    parents = set()
    with open('input.txt', 'r') as file_in:
        count_childs = int(file_in.readline().strip())
        for i in range(count_childs - 1):
            child, parent = file_in.readline().strip().split()
            if parent in parent_child:
                parent_child[parent].append(child)
            else:
                parent_child[parent] = [child]
            childs.add(child)
            parents.add(parent)
    root_parent = (parents - (childs & parents)).pop()

    result = dfs(parent_child, root_parent)
    new_result = sorted(result)
    for person, depth in new_result:
        print(person, depth)
    # print(*sorted(result), sep='\n')


if __name__ == '__main__':
    main()
