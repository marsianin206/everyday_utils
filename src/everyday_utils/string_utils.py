import re
import unicodedata
from typing import Optional

def truncate_string(s: str, max_length: int = 100, suffix: str = '...') -> str:
    """
    Усекает строку до максимальной длины, добавляя суффикс при необходимости.

    :param s: Строка для усечения.
    :param max_length: Максимальная длина.
    :param suffix: Суффикс для добавления при усечении.
    :return: Усеченная строка.
    """
    if len(s) <= max_length:
        return s
    return s[:max_length - len(suffix)] + suffix

def remove_punctuation(s: str) -> str:
    """
    Удаляет знаки препинания из строки.

    :param s: Строка для очистки.
    :return: Очищенная строка.
    """
    return re.sub(r'[^\w\s]', '', s)

def slugify(s: str) -> str:
    """
    Преобразует строку в URL-дружелюбный слаг (нижний регистр, дефисы, без специальных символов).

    :param s: Строка для преобразования.
    :return: Слаг.
    """
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii')
    s = re.sub(r'[^\w\s-]', '', s.lower())
    return re.sub(r'[-\s]+', '-', s).strip('-')