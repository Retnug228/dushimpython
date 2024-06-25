# Дан массив целых чисел, необходимо определить есть ли в нем такая последовательность,
# что i < j < k и nums[i] < nums[k] < nums[j]
#
# Пример: nums = [1,2,3,4], вывод: False
# Пример: nums = [3,1,4,2], вывод: True, пояснение: [1, 4, 2]
# Пример: nums = [-1,3,2,0], вывод: True, пояснение: имеется три нужных последовательности [-1, 3, 2], [-1, 3, 0] и [-1, 2, 0]

def find_132_pattern(nums):
    if len(nums) < 3:
        return False

    third = float('-inf')
    stack = []

    for i in range(len(nums) - 1, -1, -1):
        if nums[i] < third:
            return True
        while stack and nums[i] > stack[-1]:
            third = stack.pop()
        stack.append(nums[i])

    return False


# Примеры использования:
print(find_132_pattern([1, 2, 3, 4]))  # Вывод: False
print(find_132_pattern([3, 1, 4, 2]))  # Вывод: True
print(find_132_pattern([-1, 3, 2, 0]))  # Вывод: True
