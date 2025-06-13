def is_year_leap(year):
    # Год високосный, если делится на 4 без остатка
    return year % 4 == 0


# Выберите любой год для проверки
year_to_check = 2024

# Вызов функции и сохранение результата
result = is_year_leap(year_to_check)

# Вывод результата
print(f"год {year_to_check}: {result}")
