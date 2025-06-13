from address import Address
from mailing import Mailing

# Создаём адреса отправления и получателя
to_addr = Address("123456", "Москва", "Ленина", "10", "5")
from_addr = Address("654321", "Санкт-Петербург", "Невский", "20", "10")

# Создаём почтовое отправление
mail = Mailing(to_addr, from_addr, 350.5, "TRK123456789")

# Выводим информацию об отправлении с переносами строк
print(
    f"Отправление {mail.track} из {mail.from_address.index}, "
    f"{mail.from_address.city}, {mail.from_address.street}, "
    f"{mail.from_address.house} - {mail.from_address.apartment} "
    f"в {mail.to_address.index}, {mail.to_address.city}, "
    f"{mail.to_address.street}, {mail.to_address.house} - "
    f"{mail.to_address.apartment}. Стоимость {mail.cost} рублей."
)
