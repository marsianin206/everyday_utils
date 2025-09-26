import re
from typing import List

def is_valid_email(email: str) -> bool:
    """
    Проверяет, является ли строка действительным email-адресом с использованием надежного регулярного выражения.

    :param email: Email для проверки.
    :return: True, если email действителен, иначе False.
    """
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email.strip()))

def is_palindrome(s: str) -> bool:
    """
    Проверяет, является ли строка палиндромом (игнорирует регистр, пробелы и знаки препинания).

    :param s: Строка для проверки.
    :return: True, если строка является палиндромом, иначе False.
    """
    cleaned = re.sub(r'[^A-Za-z0-9]', '', s.lower())
    return cleaned == cleaned[::-1]