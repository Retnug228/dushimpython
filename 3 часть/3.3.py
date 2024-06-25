# Дан список строк, необходимо вывести список из списков,
# которые представляет из себя анаграммы.
#
# Пример: strs = ["eat","tea","tan","ate","nat","bat"], вывод: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Пример: strs = [""], вывод [[""]]
# Пример: strs = ["a"], вывод [["a"]]

def group_anagrams(strs):
    # Функция для сортировки строки
    def sort_string(s):
        return ''.join(sorted(s))

    anagrams = {}

    for s in strs:
        # Сортируем строку и используем её как ключ
        sorted_str = sort_string(s)
        if sorted_str in anagrams:
            anagrams[sorted_str].append(s)
        else:
            anagrams[sorted_str] = [s]

    # Возвращаем значения словаря в виде списка списков
    return list(anagrams.values())


# Примеры использования
strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs1))  # Вывод: [["eat","tea","ate"],["tan","nat"],["bat"]]

strs2 = [""]
print(group_anagrams(strs2))  # Вывод: [[""]]

strs3 = ["a"]
print(group_anagrams(strs3))  # Вывод: [["a"]]
