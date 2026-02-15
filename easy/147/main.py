from collections import deque


def main():
    with open('input.txt', 'r') as file_in:
        queue = deque()
        while True:
            operation = file_in.readline().strip().split()
            command = operation[0]
            if command == 'push_front':
                value = operation[1]
                queue.appendleft(value)
                print('ok')
            elif command == 'push_back':
                value = operation[1]
                queue.append(value)
                print('ok')
            elif command == 'size':
                print(len(queue))
            elif command == 'clear':
                queue.clear()
                print('ok')
            elif command == 'exit':
                print('bye')
                break
            else:
                if len(queue) == 0:
                    print('error')
                    continue
                if command == 'pop_front':
                    print(queue.popleft())
                elif command == 'pop_back':
                    print(queue.pop())
                elif command == 'front':
                    print(queue[0])
                elif command == 'back':
                    print(queue[-1])


if __name__ == '__main__':
    main()
