import sys


class CorrectSeq:
    def __init__(self, seq: tuple[int]):
        self.seq = seq

    def swap_pos(self):
        even_odd = []
        odd_even = []
        for i in range(len(self.seq)):
            if ((i + 1) % 2 == 1) and (self.seq[i] % 2 == 0):
                even_odd.append(i + 1)
            elif ((i + 1) % 2 == 0) and (self.seq[i] % 2 == 1):
                odd_even.append(i + 1)
        if (len(even_odd) == 1) and (len(odd_even) == 1):
            return even_odd[0], odd_even[0]
        elif (len(even_odd) == 0) and (len(odd_even) == 0) and (len(self.seq) > 2):
            return 1, 3
        else:
            return -1, -1


def main():
    # with open('input.txt', 'r') as file_in:
    #     n = int(file_in.readline().strip())
    #     heights = tuple(map(int, file_in.readline().strip().split()))
    n = int(sys.stdin.readline().strip())
    heights = tuple(map(int, sys.stdin.readline().strip().split()))
    cor_seq = CorrectSeq(heights)
    print(*cor_seq.swap_pos())


if __name__ == '__main__':
    main()
