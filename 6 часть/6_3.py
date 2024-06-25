# Ограничим правильное использование заглавных букв тремя вариантами: 
# в слове все заглавные (USSR), в слове все строчные (mother), в слове только первая заглавная (Yandex).

# Дана строка, необходимо вывести True, если использование заглавных букв в нем правильное,
# False - в противном случае.

# Пример: word = "USSR", вывод: True
# Пример: word = "GandR", вывод: False

import re

def uppers(word):
    return bool(re.fullmatch(r'[A-Z]+', word))

def lowers(word):    
    return bool(re.fullmatch(r'[a-z]+', word))

def mid(word):    
    return bool(re.fullmatch(r'[A-Z]{1}[a-z]+', word))

