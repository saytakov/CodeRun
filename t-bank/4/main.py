class max_diff:
    def __init__(self, numbers: list[str]):
        self.digits_of_number: list[list[str]] = self._build_digits_of_number(numbers)

    def _build_digits_of_number(self, numbers: list[str]):
        digits_of_number: list[list[str]] = [[] for _ in range(9)]
        for number in numbers:
            number = number[::-1]
            for i_digit in range(len(number)):
                digits_of_number[i_digit].append(number[i_digit])
        for i in range(len(digits_of_number)):
            digits_of_number[i].sort()
        return digits_of_number

    def find_max_diff(self, k: int):
        result = 0
        count = 0
        for i in range(len(self.digits_of_number) - 1, -1, -1):
            for j in range(len(self.digits_of_number[i])):
                if (el := self.digits_of_number[i][j]) != '9':
                    result += (9 - int(el)) * 10 ** i
                    count += 1
                    if count == k:
                        return result
        return result


def main():
    # with open('input.txt', 'r') as file_in:
    #     n, k = map(int, file_in.readline().strip().split())
    #     numbers: list[str] = list(file_in.readline().strip().split())
    n, k = map(int, input().strip().split())
    numbers: list[str] = list(input().strip().split())
    res_max_diff = max_diff(numbers)
    result = res_max_diff.find_max_diff(k)
    print(result)


if __name__ == '__main__':
    main()
