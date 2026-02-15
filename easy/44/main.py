from collections import deque


def bfs_number(start: str, goal: str) -> list[str]:
    queue = deque([[start]])
    visited = set()

    while queue:
        numbers: list[str] = queue.popleft()
        number = numbers[-1]
        if number == goal:
            return numbers

        if number in visited:
            continue

        visited.add(number)

        if int(number[0]) < 9:
            new_number_1 = str(int(number[0]) + 1) + number[1:]
            new_numbers_1 = list(numbers)
            new_numbers_1.append(new_number_1)
            queue.append(new_numbers_1)

        if int(number[-1]) > 1:
            new_number_2 = number[:-1] + str(int(number[-1]) - 1)
            new_numbers_2 = list(numbers)
            new_numbers_2.append(new_number_2)
            queue.append(new_numbers_2)

        new_number_right = number[-1] + number[:-1]
        new_numbers_right = list(numbers)
        new_numbers_right.append(new_number_right)
        queue.append(new_numbers_right)

        new_number_left = number[1:] + number[0]
        new_numbers_left = list(numbers)
        new_numbers_left.append(new_number_left)
        queue.append(new_numbers_left)

    return []


def main():
    with open('input.txt', 'r') as file_in:
        start = file_in.readline().strip()
        goal = file_in.readline().strip()

    result = bfs_number(start, goal)

    print('\n'.join(result))


if __name__ == '__main__':
    main()
