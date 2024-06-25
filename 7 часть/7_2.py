# Даны две строки s1 и s2. Необходимо вернуть True, если хотя бы одна из перестановок s1
#  содержится в s2. Строки могут содержать только латинские строчные буквы.

# Пример: s1 = "ab", s2 = "eidbaooo", вывод: True
# Пример: s1 = "aooob", s2 = "eidboaoo", вывод: True
# Пример: s1 = "ab", s2 = "eidboaoo", вывод: False

from itertools import permutations

def contains(s1, s2):
    for p in list(permutations(s1, len(s1))):
        if ''.join(p) in s2: return True
    return False
    
print(contains('ab', 'eidboaoo'))