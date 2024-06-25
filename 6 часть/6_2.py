# Дано целое число и список из целых чисел. Необходимо вывести число комбинаций, 
# которыми можно разложить заданное число числами из заданного списка. 
# Число из списка может использоваться неограниченное количество раз.

# Пример: amount = 5, nums = [1,2,5], вывод: 4, пояснение: 5=5, 5=2+2+1, 5=2+1+1+1, 5=1+1+1+1+1
# Пример: amount = 3, nums = [2], вывод: 0
# Пример: amount = 10, nums = [10], вывод: 1

# Динамическое программирование => эффективно

def count_combinations(amount, nums):
    # Создаем массив для хранения количества способов разложить каждое число (от 0 до самого числа включительно)
    variants = [0] * (amount + 1)
    # Число 0 можно получить единственным способом
    variants[0] = 1
    
    # Для каждого числа из списка обновляем массив variants
    for num in nums:
        for i in range(num, amount + 1):
            variants[i] += variants[i - num]
    
    return variants[amount]

print(count_combinations(5, [1, 2, 5])) 