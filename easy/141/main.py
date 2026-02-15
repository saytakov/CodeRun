from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def stack_append(self, value):
        self.stack.appendleft(value)

    def stack_back(self):
        return self.stack[0]

    def stack_pop(self):
        return self.stack.popleft()

    def stack_len(self):
        return len(self.stack)

    def stack_is_empty(self):
        if self.stack_len() == 0:
            return True
        return False


def is_correct_close_scobe(stack: Stack, rules: dict[str, str], value: str):
    if stack.stack_is_empty():
        return False
    stack_value = stack.stack_back()
    if rules[stack_value] == value:
        return True
    return False


def is_correct_sequence(scobes):
    rules = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    stack = Stack()
    for scobe in scobes:
        if scobe in rules:
            stack.stack_append(scobe)
        else:
            if is_correct_close_scobe(stack, rules, scobe):
                if stack.stack_is_empty():
                    return False
                else:
                    stack.stack_pop()
            else:
                return False
    if stack.stack_len() == 0:
        return True
    else:
        return False


def main():
    with open('input.txt', 'r') as file_in:
        scobes = file_in.readline().strip()
    if is_correct_sequence(scobes):
        print('yes')
    else:
        print('no')


if __name__ == '__main__':
    main()
