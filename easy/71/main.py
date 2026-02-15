def check_type_sequence(numbers):
    type_sequence = {
        'CONSTANT': True,
        'ASCENDING': True,
        'WEAKLY ASCENDING': True,
        'DESCENDING': True,
        'WEAKLY DESCENDING': True,
    }
    for i in range(len(numbers) - 1):
        cur_numb = numbers[i]
        next_numb = numbers[i+1]
        if cur_numb < next_numb:
            type_sequence.update(
                {
                    'CONSTANT': False,
                    'DESCENDING': False,
                    'WEAKLY DESCENDING': False,
                }
            )
        elif cur_numb > next_numb:
            type_sequence.update(
                {
                    'CONSTANT': False,
                    'ASCENDING': False,
                    'WEAKLY ASCENDING': False,
                }
            )
        else:
            type_sequence.update(
                {
                    'ASCENDING': False,
                    'DESCENDING': False,
                }
            )
        if list(type_sequence.values()).count(True) == 0:
            return 'RANDOM'
    return next(key for key, value in type_sequence.items() if value)


def main():
    with open('input.txt', 'r') as file_in:
        numbers = []
        while True:
            cur = int(file_in.readline().strip())
            if cur == -2_000_000_000:
                break
            numbers.append(cur)
    result = check_type_sequence(numbers)
    print(result)


if __name__ == '__main__':
    main()
