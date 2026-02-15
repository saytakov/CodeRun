def degree_genom_proxity(genom1, genom2):
    result = 0
    genoms2 = set()
    for i in range(len(genom2) - 1):
        genoms2.add(genom2[i] + genom2[i+1])
    for i in range(len(genom1) - 1):
        if (genom1[i] + genom1[i+1]) in genoms2:
            result += 1
    return result


def main():
    with open('input.txt', 'r') as file_in:
        str1 = file_in.readline().strip()
        str2 = file_in.readline().strip()

        result = degree_genom_proxity(str1, str2)

        print(result)


if __name__ == '__main__':
    main()
