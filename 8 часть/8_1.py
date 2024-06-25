# Для заданного целого положительного числа c определить существуют ли 
# такие числа a и b, что a * a + b * b = c.

# Пример: c = 5, вывод: True, пояснение: 1 * 1 + 2 * 2 = 5
# Пример: c = 3, вывод: False

def sumNumbers(c):
    for a in range(c):
        for b in range(a, c):
            s = a*a + b*b
            if s > c: break
            if s == c: return True
    return False

c = int(input())
print(sumNumbers(c))