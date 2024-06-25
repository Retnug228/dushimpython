import math


def find_squares(n):
    def find_numbers(target, count):
        if count == 1:
            root = int(math.sqrt(target))
            return [root] if root ** 2 == target else []

        for i in range(int(math.sqrt(target)), 0, -1):
            result = find_numbers(target - (i * i), count - 1)
            if result:
                return [i] + result

        return []

    for count in range(1, n + 1):
        result = find_numbers(n, count)
        if result:
            return result

    return -1


print(find_squares(12))
print(find_squares(29))
