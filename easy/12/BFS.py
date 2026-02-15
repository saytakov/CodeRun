from collections import deque

city_map: dict[str, list[str]] = {
    'Home': ['Park', 'School', 'Mail'],
    'Park': ['Home', 'Museum', 'Cafe'],
    'School': ['Home', 'Library', 'Mail'],
    'Mail': ['Home', 'School', 'Hospital'],
    'Library': ['School', 'Hospital'],
    'Hospital': ['Library', 'Mail', 'Office'],
    'Cafe': ['Park', 'Theater', 'Office'],
    'Museum': ['Park', 'Shop'],
    'Shop': ['Museum', 'Theater'],
    'Theater': ['Shop', 'Cafe'],
    'Office': ['Cafe', 'Hospital']
}


def main(city_map: dict[str, list[str]]):
    start: str = 'Home'
    goal: str = 'Theater'
    minimal_path: list[str] | None = search_path(city_map, start, goal)
    print(minimal_path)


def search_path(
    city_map: dict[str, list[str]],
    start: str, goal: str
) -> list[str] | None:
    queue: deque[list[str]] = deque([[start]])
    visited: set[str] = set()

    while queue:
        path: list[str] = queue.popleft()
        node: str = path[-1]

        if node in visited:
            continue

        if node == goal:
            return path

        visited.add(node)

        for neighbor in city_map.get(node, []):
            new_path: list[str] = list(path)
            new_path.append(neighbor)
            queue.append(new_path)

    return None


if __name__ == '__main__':
    main(city_map)
