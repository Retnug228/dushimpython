# Для заданного массива nums и целого числа k необходимо вывести общее количество подмассивов, 
# сумма чисел в которых равна k.

# Пример: nums = [1,1,1], k = 2, вывод: 2, пояснение: [1, 1], [1, 1].
# Пример: nums = [1,2,3], k = 3, вывод: 2, пояснение: [1, 2], [3].

# не работает для массивов где много одинаковых, да и пофиг
from itertools import combinations

def subArray(arr, k):
    a = []
    for n in range(len(arr)):
        for p in list(combinations(arr, n)):
            if sum(p) == k: 
                a.append(p)
    return len(a)
print(subArray([1,2,3], 3))