# Имеется массив целых чисел numbers. Необходимо найти все такие тройки:
# [numbers[i], numbers[j], numbers[k]], где i != j, j != k, k != i
# и сумма numbers[i] + numbers[j] + numbers[k] = 0

def triples(numbers):
    result = []
    for i in range(0, len(numbers)-2):
        for j in range(i+1, len(numbers)-1):
            for k in range(j+1, len(numbers)):
                if numbers[i]!=numbers[j] and numbers[i]!=numbers[k] and numbers[k]!=numbers[j] and (numbers[i]+numbers[j]+numbers[k])==0:
                    result.append([numbers[i], numbers[j], numbers[k]])
    return result

# Пример использования
numbers = [4, -1, 7, 0, 1, 2, -1, 5]
print(triples(numbers))
