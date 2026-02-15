def main():
    with open('input.txt', 'r') as file_in:
        count_anya, count_borya = map(int, file_in.readline().strip().split())
        cubes_anya = set()
        cubes_borya = set()
        for _ in range(count_anya):
            cubes_anya.add(int(file_in.readline().strip()))
        for _ in range(count_borya):
            cubes_borya.add(int(file_in.readline().strip()))
    union_cubes = cubes_anya & cubes_borya
    only_anya = cubes_anya - union_cubes
    only_borya = cubes_borya - union_cubes
    print(len(union_cubes))
    print(*sorted(union_cubes))
    print(len(only_anya))
    print(*sorted(only_anya))
    print(len(only_borya))
    print(*sorted(only_borya))


if __name__ == '__main__':
    main()
