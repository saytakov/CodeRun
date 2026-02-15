def letter_add_or_create(letter, dictinary):
    if letter in dictinary:
        dictinary[letter] += 1
    else:
        dictinary[letter] = 1


def add_or_remove_targets(letter, cur_count_letter_first, count_letter_second, cur_target_count):
    if (
        (letter not in count_letter_second)
        or (cur_count_letter_first[letter] > count_letter_second[letter])
    ):
        cur_target_count.add(letter)
    else:
        cur_target_count.discard(letter)


def can_play(first_str, second_str, length_str):
    len_first = len(first_str)
    len_second = len(second_str)
    if (length_str > len_first) or (length_str > len_second):
        return False

    count_letter_second = {}
    for letter in second_str:
        letter_add_or_create(letter, count_letter_second)

    cur_count_letter_first = {}
    cur_target_count: set[str] = set()

    for i in range(length_str):
        letter = first_str[i]
        letter_add_or_create(letter, cur_count_letter_first)
        add_or_remove_targets(letter, cur_count_letter_first, count_letter_second, cur_target_count)

    if len(cur_target_count) == 0:
        return True

    left = 1
    right = length_str
    while right < len_first:
        old_left_letter = first_str[left - 1]
        cur_count_letter_first[old_left_letter] -= 1
        new_right_letter = first_str[right]
        letter_add_or_create(new_right_letter, cur_count_letter_first)
        add_or_remove_targets(letter, cur_count_letter_first, count_letter_second, cur_target_count)
        if len(cur_target_count) == 0:
            return True
        left += 1
        right += 1

    return False


def main():
    with open('input.txt', 'r') as file_in:
        length_str = int(file_in.readline().strip())
        first_str = file_in.readline().strip()
        second_str = file_in.readline().strip()

    if can_play(first_str, second_str, length_str):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
