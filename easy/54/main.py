def main():
    unique = set()
    all_now = set()
    with open('input.txt', 'r') as file_in:
        count_pupils: int = int(file_in.readline())
        for i in range(count_pupils):
            count_language = int(file_in.readline())
            lang_pupil = set()
            for _ in range(count_language):
                language = file_in.readline().strip()
                unique.add(language)
                lang_pupil.add(language)
            if i == 0:
                all_now = lang_pupil
            else:
                all_now = all_now & lang_pupil
    print(len(all_now))
    print(*all_now, sep='\n')
    print(len(unique))
    print(*unique, sep='\n')


# def main():
#     unique = set()
#     languages = {}
#     all_now = set()
#     with open('input.txt', 'r') as file_in:
#         count_pupils: int = int(file_in.readline())
#         for _ in range(count_pupils):
#             count_language = int(file_in.readline())
#             for _ in range(count_language):
#                 language = file_in.readline().strip()
#                 unique.add(language)
#                 if language not in languages:
#                     languages[language] = 1
#                 else:
#                     languages[language] += 1
#     for key, value in languages.items():
#         if value == count_pupils:
#             all_now.add(key)
#     result = ''
#     result += f'{len(all_now)}\n'
#     for lang in all_now:
#         result += f'{lang}\n'
#     result += f'{len(unique)}\n'
#     for lang in unique:
#         result += f'{lang}\n'
#     print(result)


if __name__ == '__main__':
    main()
