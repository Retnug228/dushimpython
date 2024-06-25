# Дана строка из цифр. Необходимо восстановить из нее все возможные корректные IP адреса.
# Нельзя удалять в строке или изменять порядк цифр в ней.
#
# Пример: "25525511135", вывод: ["255.255.11.135","255.255.111.35"]
# Пример: "0000", вывод: ["0.0.0.0"]
# Пример: "101023", вывод: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

def restore_ip_addresses(s):
    def is_valid(segment):
        # Сегмент должен быть числом от 0 до 255 и не содержать ведущих нулей
        return int(segment) <= 255 and (segment == "0" or segment[0] != "0")

    def backtrack(start=0, path=[]):
        # Если путь содержит 4 сегмента и мы использовали все символы строки, добавляем результат
        if len(path) == 4:
            if start == len(s):
                result.append(".".join(path))
            return

        # Пробуем все возможные сегменты длиной от 1 до 3 символов
        for length in range(1, 4):
            if start + length <= len(s):
                segment = s[start:start + length]
                if is_valid(segment):
                    backtrack(start + length, path + [segment])

    result = []
    backtrack()
    return result


# Примеры использования:
print(restore_ip_addresses("25525511135"))  # Вывод: ["255.255.11.135", "255.255.111.35"]
print(restore_ip_addresses("0000"))  # Вывод: ["0.0.0.0"]
print(restore_ip_addresses("101023"))  # Вывод: ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
