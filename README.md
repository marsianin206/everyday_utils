# Everyday Utils

Легковесная библиотека без внешних зависимостей, содержащая полезные утилиты для повседневного программирования на Python. Включает инструменты для работы с паролями, строками, файлами, валидацией, хешированием, датами и многим другим.

## Установка

```bash
pip install everyday-utils



Примеры использования
pythonfrom everyday_utils import generate_password, is_valid_email, human_readable_size

password = generate_password(length=16)
print(password)  # Например: 'A1b2C3d4E5f6G7h8'

print(is_valid_email("test@example.com"))  # True

print(human_readable_size(1024 * 1024))  # '1.00MB'


Модули

password_utils: Генерация паролей.
validation_utils: Валидация email, проверка палиндромов и т.д.
file_utils: Работа с размерами файлов и JSON.
datetime_utils: Форматирование даты и времени.
hash_utils: Хеширование строк.
random_utils: Случайный выбор и обработка списков.
string_utils: Манипуляции со строками (усечение, очистка, создание слагов).