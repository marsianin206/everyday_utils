import random
import string
import re
from typing import Optional

def generate_password(length: int = 12, include_upper: bool = True, include_lower: bool = True,
                      include_digits: bool = True, include_symbols: bool = True) -> str:
    """
    Генерирует случайный пароль с указанными критериями. Гарантирует наличие хотя бы одного символа каждого выбранного типа.

    :param length: Длина пароля (минимум 1).
    :param include_upper: Включать заглавные буквы.
    :param include_lower: Включать строчные буквы.
    :param include_digits: Включать цифры.
    :param include_symbols: Включать символы.
    :return: Сгенерированный пароль.
    """
    if length < 1:
        raise ValueError("Длина пароля должна быть не менее 1.")

    characters = ''
    if include_upper:
        characters += string.ascii_uppercase
    if include_lower:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("Необходимо выбрать хотя бы один тип символов.")

    password = ''.join(random.choice(characters) for _ in range(length))

    # Гарантия наличия хотя бы одного символа каждого выбранного типа
    if include_upper and not re.search(r'[A-Z]', password):
        password = _ensure_char_type(password, string.ascii_uppercase)
    if include_lower and not re.search(r'[a-z]', password):
        password = _ensure_char_type(password, string.ascii_lowercase)
    if include_digits and not re.search(r'\d', password):
        password = _ensure_char_type(password, string.digits)
    if include_symbols and not re.search(r'[!@#$%^&*()_+\-=\[\]{};:"\\|,.<>/?]', password):
        password = _ensure_char_type(password, string.punctuation)

    return password

def _ensure_char_type(password: str, char_set: str) -> str:
    """Вспомогательная функция для добавления хотя бы одного символа из набора."""
    pos = random.randint(0, len(password) - 1)
    return password[:pos] + random.choice(char_set) + password[pos + 1:]