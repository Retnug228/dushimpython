# Дан массив из целых чисел. Необходимо найти максимальную сумму подряд стоящих элементов.
#
# Пример: [-2,1,-3,4,-1,2,1,-5,4], вывод: 6, пояснение: [4, -1, 2, 1]
# Пример: [1], вывод: 1, пояснение: [1]
# Пример: [5,4,-1,7,8], вывод: 23, пояснение: [5,4,-1,7,8]

def max_subarray_sum(nums):
    if not nums:
        return 0

    # Инициализируем текущую и максимальную суммы первым элементом массива
    current_sum = max_sum = nums[0]

    # Проходим по остальным элементам массива
    for num in nums[1:]:
        # Обновляем текущую сумму: либо начинаем новый подмассив, либо продолжаем текущий
        current_sum = max(num, current_sum + num)
        # Обновляем максимальную сумму, если текущая сумма больше
        max_sum = max(max_sum, current_sum)

    return max_sum

# Примеры использования:
print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Вывод: 6
print(max_subarray_sum([1]))  # Вывод: 1
print(max_subarray_sum([5, 4, -1, 7, 8]))  # Вывод: 23
