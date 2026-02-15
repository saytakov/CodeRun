def main():
    with open('input.txt', 'r') as file_in:
        print(len(set(file_in.readline().strip().split())))


if __name__ == '__main__':
    main()
