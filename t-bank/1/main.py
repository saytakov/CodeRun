def main():
    a, b, c, d = map(int, input().strip().split())
    if d > b:
        print(a + c * (d - b))
    else:
        print(a)


if __name__ == '__main__':
    main()
