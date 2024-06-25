# Имеется массив целых чисел numbers.
# Необходимо найти все последовательности в массиве (подряд стоящие числа),
# сумма которых равна заданному числу S.

def sequences(numers, s):
    result = []
    for start_index in range(0, len(numbers)-1):
        for end_index in range(start_index, len(numbers)+1):
            if sum(numbers[start_index:end_index])==s:
                   result.append(numbers[start_index:end_index])
    return result

#пример использования
numbers = [4,-1,7,0,1,2,-1,5]
s = 3
print(sequences(numbers, s))
