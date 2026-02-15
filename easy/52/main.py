def search_word(dictinary: dict[str, str], target: str):
    if target in dictinary.keys():
        return dictinary[target]
    else:
        return next(key for key, value in dictinary.items() if value == target)


def main():
    with open('input.txt', 'r') as file_in:
        count = int(file_in.readline().strip())
        dictinary = {}
        for _ in range(count):
            word_1, word_2 = file_in.readline().strip().split()
            dictinary[word_1] = word_2
        target = file_in.readline().strip()

        result = search_word(dictinary, target)

        print(result)


if __name__ == '__main__':
    main()
