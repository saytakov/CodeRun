# def search_table(width, height, count):
#     result = [0, 0]
#     for i in range(2):
#         if i == 0:
#             max_side = max(width, height)
#             min_side = min(width, height)
#         else:
#             max_side = min(width, height)
#             min_side = max(width, height)
#         left = 1
#         right = count
#         while True:
#             i_cur_value = (left + right) // 2
#             value_count_on_space = ((max_side*(i_cur_value)) // min_side) * (i_cur_value)
#             value_space = max_side * i_cur_value
#             if value_count_on_space == count:
#                 result[i] = value_space
#                 break
#             elif value_count_on_space > count:
#                 right = i_cur_value
#             else:
#                 left = i_cur_value + 1
#             if (left == right) and (value_count_on_space != count):
#                 if value_count_on_space < count:
#                     result[i] = max_side * (i_cur_value + 1)
#                     break
#                 else:
#                     result[i] = value_space
#                     break
#     return min(result)


def search_table(width, height, count):
    left = min(width, height)
    right = max(width, height) * count
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        if (mid // width) * (mid // height) >= count:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


def main():
    with open('input.txt', 'r') as file_in:
        width, height, count = map(int, file_in.readline().strip().split())
    result = search_table(width, height, count)
    print(result)


if __name__ == '__main__':
    main()
