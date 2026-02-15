from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

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

    def push(self, value):
        self.stack.appendleft(value)
        return


def correct_sequence(sequence: tuple[int, ...]):
    wagons_in_dead_end = Stack()
    cur_wagon = 1
    for number in sequence:
        if number == cur_wagon:
            cur_wagon += 1
            while True:
                if wagons_in_dead_end.is_empty():
                    break
                if wagons_in_dead_end.back() == cur_wagon:
                    cur_wagon += 1
                    wagons_in_dead_end.pop()
                else:
                    break
        else:
            wagons_in_dead_end.push(number)
    if wagons_in_dead_end.is_empty():
        return True
    return False


def main():
    with open('input.txt', 'r') as file_in:
        count_wagons = int(file_in.readline().strip())
        number_wagons = tuple(map(int, file_in.readline().strip().split()))
    if correct_sequence(number_wagons):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
