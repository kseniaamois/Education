# Импортируем класс User из файла user.py
from user import User

# Создаём экземпляр класса User
my_user = User("Иван", "Иванов")

# Вызываем методы объекта
my_user.print_first_name()  # Иван
my_user.print_last_name()   # Иванов
my_user.print_full_name()   # Иван Иванов
