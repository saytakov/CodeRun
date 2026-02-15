def is_increasing_sequence(numbers):
    prev = next(numbers)
    for number in numbers:
        if number <= prev:
            return 'NO'
        else:
            prev = number
    return 'YES'


def main():
    with open('input.txt', 'r') as file_in:
        generator_numbers = map(int, file_in.readline().strip().split())
    print(is_increasing_sequence(generator_numbers))


if __name__ == '__main__':
    main()
