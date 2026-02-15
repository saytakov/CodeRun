from collections import deque


def pyanica(first: deque[int], second: deque):
    moves = 0
    while True:
        if len(first) == 0:
            return 'second', moves
        elif len(second) == 0:
            return 'first', moves
        elif moves >= 10**6:
            return 'botva',
        card_first = first.popleft()
        card_second = second.popleft()
        extends_card = (card_first, card_second)
        if (card_first > card_second):
            if (card_first == 9) and (card_second == 0):
                second.extend(extends_card)
            else:
                first.extend(extends_card)
        else:
            if (card_first == 0) and (card_second == 9):
                first.extend(extends_card)
            else:
                second.extend(extends_card)
        moves += 1


def main():
    with open('input.txt', 'r') as file_in:
        first = deque(map(int, file_in.readline().strip().split()))
        second = deque(map(int, file_in.readline().strip().split()))
    reuslt = pyanica(first, second)
    print(*reuslt)


if __name__ == '__main__':
    main()
