def checking_capacity(a, b, c, d, e):
    count_de = [0, 0]
    abc = [a, b, c]
    de = [d, e]
    for i in range(2):
        count_de[i] = [True if abc[j] <= de[i] else False for j in range(len(abc))].count(True)
    if count_de[0] >= 1 and count_de[1] >= 2 or count_de[0] >= 2 and count_de[1] >= 1:
        return 'YES'
    return 'NO'


def main():
    with open('input.txt', 'r') as file_in:
        a = int(file_in.readline().strip())
        b = int(file_in.readline().strip())
        c = int(file_in.readline().strip())
        d = int(file_in.readline().strip())
        e = int(file_in.readline().strip())

    print(checking_capacity(a, b, c, d, e))


if __name__ == '__main__':
    main()
