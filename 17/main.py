class SortedStack:
    def __init__(self, seq: list[float]):
        self.seq = seq

    def sort(self) -> int:
        stack = []
        last = float('-inf')
        self.seq.append(float('inf'))
        for i in range(len(self.seq) - 1):
            if self.seq[i] < last:
                return 0
            if self.seq[i] >= self.seq[i + 1]:
                stack.append(self.seq[i])
                continue
            last = self.seq[i]
            while stack:
                if (stack[-1] <= self.seq[i + 1]) and (stack[-1] >= last):
                    el = stack.pop()
                    last = el
                else:
                    break
        return int(not bool(len(stack)))


def main():
    with open('input.txt', 'r') as file_in:
        count_req = int(file_in.readline().strip())
        for _ in range(count_req):
            seq = SortedStack(list(map(
                float,
                file_in.readline().strip().split()
                ))[1:])
            print(seq.sort())


if __name__ == '__main__':
    main()
