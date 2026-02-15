def check_added(target: str, numbers: list[str]):
    target = (target
              .replace('(', '')
              .replace(')', '')
              .replace('-', '')
              .replace('+', ''))
    if len(target) == 7:
        target = '495' + target
    else:
        target = target[1:]
    for number in numbers:
        number = (number
                  .replace('(', '')
                  .replace(')', '')
                  .replace('-', '')
                  .replace('+', ''))
        if len(number) == 7:
            number = '495' + number
        else:
            number = number[1:]
        if number == target:
            print('YES')
        else:
            print('NO')


def main():
    with open('input.txt', 'r') as file_in:
        numbers = []
        new_number = file_in.readline().strip()
        numbers.append(file_in.readline().strip())
        numbers.append(file_in.readline().strip())
        numbers.append(file_in.readline().strip())
    check_added(new_number, numbers)


if __name__ == '__main__':
    main()
