# Дана строка s и массив строк wordDict.
# Необходимо вернуть True, если слово s можно составить из слов в массиве wordDict.
# Слово из workDict может быть использовано в s любое количество раз.
#
# Пример: s = "applepenapple", wordDict = ["apple","pen"], вывод: True
# Пример: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"], вывод: False

def word_break(s, wordDict):
    word_set = set(wordDict)  # Преобразуем список слов в множество для быстрого поиска
    dp = [False] * (len(s) + 1)
    dp[0] = True  # Пустая строка всегда может быть составлена

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[len(s)]


# Примеры использования:
print(word_break("applepenapple", ["apple", "pen"]))  # Вывод: True
print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # Вывод: False
