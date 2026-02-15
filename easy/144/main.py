from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, value):
        self.stack.appendleft(value)
        return

    def back(self):
        return self.stack[0]

    def length(self):
        return len(self.stack)

    def is_empty(self):
        if self.length() == 0:
            return True
        return False

    def pop(self):
        return self.stack.popleft()


def removels(towns, count_town):
    stack = Stack()
    result = []
    for i in range(count_town):
        while True:
            if stack.is_empty():
                break
            if stack.back()[1] > towns[i]:
                index_town, town = stack.pop()
                result.append((index_town, town, i))
            else:
                break
        stack.push((i, towns[i]))
    while not stack.is_empty():
        index_town, town = stack.pop()
        result.append((index_town, town, -1))
    return sorted(result)


def main():
    with open('input.txt', 'r') as file_in:
        count_town = int(file_in.readline().strip())
        towns = tuple(map(int, file_in.readline().strip().split()))
    towns_res = removels(towns, count_town)
    result = ''
    for town in towns_res:
        result += f'{town[2]} '
    print(result)


if __name__ == '__main__':
    main()
