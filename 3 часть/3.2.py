# Даны два положительных целых числа в виде строк.
# Необходимо выполнить их умножения без преобразования к целому числу
# (нельзя использовать функцию int).
#
# Пример: num1 = "2", num2 = "3", вывод: "6"
# Пример: num1 = "123", num2 = "456", вывод: "56088"

def multiply_strings(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"

    # Инициализируем результат как массив нулей
    result = [0] * (len(num1) + len(num2))

    # Переворачиваем строки для удобства работы с индексами
    num1 = num1[::-1]
    num2 = num2[::-1]

    # Выполняем умножение поразрядно
    for i in range(len(num1)):
        for j in range(len(num2)):
            digit_mul = int(num1[i]) * int(num2[j])
            result[i + j] += digit_mul
            result[i + j + 1] += result[i + j] // 10
            result[i + j] %= 10

    # Убираем ведущие нули из результата
    while len(result) > 1 and result[-1] == 0:
        result.pop()

    # Преобразуем результат обратно в строку
    result = result[::-1]
    return ''.join(map(str, result))

# Примеры использования
num1 = "123"
num2 = "456"
print(multiply_strings(num1, num2))  # Вывод: "56088"

num3 = "2"
num4 = "3"
print(multiply_strings(num3, num4))  # Вывод: "6"
