def main():
    with open('input.txt', 'r') as file_in:
        xyz = set(file_in.readline().strip().split())
        target = set(file_in.readline().strip())
        union = xyz & target
        print(len(target) - len(union))
        asd = target - xyz
        print(len(asd))


if __name__ == '__main__':
    main()
