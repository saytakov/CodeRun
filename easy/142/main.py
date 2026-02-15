from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, value) -> None:
        self.stack.appendleft(value)

    def length(self):
        return len(self.stack)

    def is_empty(self):
        if self.length() == 0:
            return True
        return False

    def pop(self):
        return self.stack.popleft()


def postfix_calculate(equation):
    stack = Stack()
    operator = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
    }
    for char in equation:
        if char not in operator:
            stack.push(int(char))
        else:
            if stack.is_empty() or stack.length() < 2:
                return 'error'
            second = stack.pop()
            first = stack.pop()
            result = operator[char](first, second)
            stack.push(result)
    return stack.pop()


def main():
    with open('input.txt', 'r') as file_in:
        equation = file_in.readline().strip().split()
    answer = postfix_calculate(equation)
    print(answer)


if __name__ == '__main__':
    main()
