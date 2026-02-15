def main():
    with open('input.txt', 'r') as file_in:
        set1 = set(map(int, file_in.readline().strip().split()))
        set2 = set(map(int, file_in.readline().strip().split()))
        print(' '.join(map(str, sorted(set1 & set2))))


if __name__ == '__main__':
    main()
