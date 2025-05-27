from smartphone import Smartphone

# Создаём список из пяти экземпляров класса Smartphone
catalog = [
    Smartphone("Apple", "iPhone 13", "+79161234567"),
    Smartphone("Samsung", "Galaxy S21", "+79261234567"),
    Smartphone("Xiaomi", "Redmi Note 10", "+79361234567"),
    Smartphone("OnePlus", "9 Pro", "+79461234567"),
    Smartphone("Google", "Pixel 6", "+79561234567"),
]

# Выводим каталог телефонов в формате "<марка> - <модель>. <номер телефона>"
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
