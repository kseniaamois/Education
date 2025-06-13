import math


def square(side):
    # Вычисляем площадь квадрата
    area = side * side
    # Округляем результат вверх и возвращаем
    return math.ceil(area)


# Пример вызова функции
side_length = 4.3
result = square(side_length)

print(f"Площадь квадрата со стороной {side_length} равна {result}")
