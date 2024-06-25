# В заданном массиве строк (без повторений) найти слова, которые являются производным словом из данного массива.
# Производное слово - это слово, которое состоит из по-крайней мере двух слов данного массива.
#
# Пример: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"], вывод: ["catsdogcats","dogcatsdog","ratcatdogcat"]
# Пример: words = ["cat","dog","catdog"], вывод: ["catdog"]

def findAllConcatenatedWords(words):
    word_set = set(words)
    result = []

    def canForm(word):
        if word in memo:
            return memo[word]

        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in word_set and (suffix in word_set or canForm(suffix)):
                memo[word] = True
                return True

        memo[word] = False
        return False

    memo = {}
    for word in words:
        if canForm(word):
            result.append(word)

    return result


# Примеры использования:
words1 = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
words2 = ["cat", "dog", "catdog"]

print(findAllConcatenatedWords(words1))  # Вывод: ["catsdogcats", "dogcatsdog", "ratcatdogcat"]
print(findAllConcatenatedWords(words2))  # Вывод: ["catdog"]
