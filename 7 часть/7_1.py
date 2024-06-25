# Даны 4 координаты в 2-х мерной плоскости p1, p2, p3, p4 в формате [x, y]. 
# Необходимо проверять образуют ли точки квадрат.
# Квадрат имеет 4 одинаковых стороны и четыре угла по 90 градусов.

# Пример: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1], вывод: True
# Пример: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12], вывод: False
# Пример: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1], вывод: True

def p(p1, p2): 
    """ Расстояние между двумя точками """
    return ( (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 )**0.5


def isSquare(*points): 
    """ Основная программа """
    ps = set()
    start = points[0]
    for i in range(1, len(points)):
        ps.add(p(start, points[i]))

    # в квадрате между каждыми точками есть 2 уникальных длины: сторона и гипотенуза
    # если длина мн-ва == 2, то уникальных длин 2 => квадрат
    return True if len(ps) == 2 else False

p1 = [1,0]
p2 = [-1,0]
p3 = [0,1]
p4 = [0,-1]

print(isSquare(p1, p2, p3, p4))