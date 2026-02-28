from math import ceil


def main():
    # with open('input.txt', 'r') as file_in:
        # length = int(file_in.readline().strip())
    length = int(input())
    result = 0
    cur_length = length
    while cur_length != 1:
        cur_length = ceil(cur_length / 2)
        result += 1
    print(result)


if __name__ == '__main__':
    main()
