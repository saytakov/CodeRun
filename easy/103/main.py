# def min_size_table(h_1, w_1, h_2, w_2):
#     sizes_1 = [h_1, w_1]
#     sizes_2 = [h_2, w_2]
#     result = 100000000000000000000000000000000000000000000000000000000
#     min_size = ()
#     for size_1 in sizes_1:
#         for size_2 in sizes_2:
#             value = (size_1 + size_2) * max(sum(sizes_1) - size_1, sum(sizes_2) - size_2)
#             if value < result:
#                 result = value
#                 min_size = (size_1 + size_2, max(sum(sizes_1) - size_1, sum(sizes_2) - size_2))
#     return min_size

def min_size_table(h1, w1, h2, w2):
    answer = h1 + h2, w1 + w2
    for x1, y1 in ((h1, w1), (w1, h1)):
        for x2, y2 in ((h2, w2), (w2, h2)):
            x = x1 + x2
            y = max(y1, y2)
            if x * y < answer[0] * answer[1]:
                answer = x, y
    return answer


def main():
    with open('input.txt', 'r') as file_in:
        h_1, w_1, h_2, w_2 = map(int, file_in.readline().strip().split())
    result = min_size_table(h_1, w_1, h_2, w_2)
    print(' '.join(map(str, result)))


if __name__ == '__main__':
    main()
