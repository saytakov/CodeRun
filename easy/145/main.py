from collections import deque


def main():
    queue = deque()
    with open('input.txt', 'r') as file_in:
        while True:
            operation = file_in.readline().strip().split()
            command = operation[0]
            if command == 'push':
                value = operation[1]
                queue.append(value)
                print('ok')
            elif command == 'pop':
                if len(queue) == 0:
                    print('error')
                else:
                    print(queue.popleft())
            elif command == 'front':
                if len(queue) == 0:
                    print('error')
                else:
                    print(queue[0])
            elif command == 'size':
                print(len(queue))
            elif command == 'clear':
                queue.clear()
                print('ok')
            else:
                print('bye')
                break


if __name__ == '__main__':
    main()
