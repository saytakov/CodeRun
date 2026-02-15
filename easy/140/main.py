from collections import deque


def stack_push(stack: deque, value: int):
    stack.appendleft(value)
    return stack


def stack_pop(stack: deque):
    result = stack.popleft()
    return stack, result


def stack_back(stack: deque):
    return stack[0]


def stack_len(stack: deque):
    return len(stack)


def stack_clear(stack: deque):
    stack.clear()
    return stack


def stack_is_empty(stack: deque):
    if len(stack) == 0:
        return True
    return False


def main():
    with open('input.txt', 'r') as file_in:
        stack = deque()
        while True:
            operation = file_in.readline().strip().split()
            command = operation[0]
            if command == 'push':
                value: int = int(operation[1])
                stack = stack_push(stack, value)
                print('ok')
            elif command == 'pop':
                if stack_is_empty(stack):
                    print('error')
                else:
                    stack, answer = stack_pop(stack)
                    print(answer)
            elif command == 'back':
                if stack_is_empty(stack):
                    print('error')
                else:
                    print(stack_back(stack))
            elif command == 'size':
                print(stack_len(stack))
            elif command == 'clear':
                stack = stack_clear(stack)
                print('ok')
            elif command == 'exit':
                print('bye')
                break


if __name__ == '__main__':
    main()
