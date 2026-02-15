def main():
    count_letter = {}
    with open('input.txt', 'r') as file_in:
        stroke = file_in.readline().strip()
    for i in range(len(stroke)):
        letter = stroke[i]
        first = i + 1
        second = len(stroke) - first + 1
        if letter not in count_letter:
            count_letter[letter] = first * second
        else:
            count_letter[letter] += first * second
    for letter, count in sorted(count_letter.items()):
        print(f'{letter}: {count}')


if __name__ == '__main__':
    main()
