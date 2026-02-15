def in_range(
    cur_section_start: int,
    cur_section_end: int,
    old_section_start: int,
    old_section_end: int,
) -> bool:
    if (
        (cur_section_start <= old_section_start <= cur_section_end)
        or (cur_section_start <= old_section_end <= cur_section_end)
        or (old_section_start <= cur_section_start <= old_section_end)
        or (old_section_start <= cur_section_end <= old_section_end)
    ):
        return True
    return False


def main():
    sectors: list[tuple[int, int]] = []
    with open('input.txt', 'r') as file_in:
        count_sectors = int(file_in.readline().strip())
        count_sections = int(file_in.readline().strip())
        for _ in range(count_sections - 1):
            if not sectors:
                sectors.append(tuple(map(int, file_in.readline().strip().split())))
            cur_section_start, cur_section_end = map(int, file_in.readline().strip().split())
            new_sectors = sectors.copy()
            for old_section_start, old_section_end in new_sectors:
                if in_range(
                    cur_section_start,
                    cur_section_end,
                    old_section_start,
                    old_section_end
                ):
                    sectors.remove((old_section_start, old_section_end))
            sectors.append((cur_section_start, cur_section_end))

    print(len(sectors))


if __name__ == '__main__':
    main()
