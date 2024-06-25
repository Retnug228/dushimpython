# #В списке из строк найти максимальный общий префикс.
#
# Пример: strs = ["flower","flow","flight"], вывод: "fl"
# Пример: strs = ["dog","racecar","car"], вывод: ""
# Считать, что в строках могут использоваться только латинские буквы.

def longest_common_prefix(strs):
    if not strs:
        return ""

    # Инициализируем префикс первой строкой из списка
    prefix = strs[0]

    # Проходим по всем строкам в списке
    for string in strs[1:]:
        # Постепенно сокращаем префикс, пока он не станет общим
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix

# Примеры использования
strs1 = ["flower", "flow", "flight"]
print(longest_common_prefix(strs1))  # Вывод: "fl"

strs2 = ["dog", "racecar", "car"]
print(longest_common_prefix(strs2))  # Вывод: ""
