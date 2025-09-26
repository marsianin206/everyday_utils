import os
import json
from typing import Dict, Any

def human_readable_size(size_in_bytes: float) -> str:
    """
    Преобразует размер файла в байтах в читаемый формат (например, KB, MB).

    :param size_in_bytes: Размер в байтах.
    :return: Строка с читаемым размером.
    """
    if size_in_bytes < 0:
        raise ValueError("Размер не может быть отрицательным.")
    if size_in_bytes == 0:
        return "0B"
    units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
    i = 0
    while size_in_bytes >= 1024 and i < len(units) - 1:
        size_in_bytes /= 1024
        i += 1
    return f"{size_in_bytes:.2f}{units[i]}"

def get_file_size(file_path: str) -> int:
    """
    Получает размер файла в байтах.

    :param file_path: Путь к файлу.
    :return: Размер в байтах или 0, если файл не существует.
    """
    if not isinstance(file_path, str):
        raise TypeError("file_path должен быть строкой.")
    if os.path.exists(file_path) and os.path.isfile(file_path):
        return os.path.getsize(file_path)
    return 0

def load_json_file(file_path: str) -> Dict[str, Any]:
    """
    Загружает JSON-файл в словарь.

    :param file_path: Путь к JSON-файлу.
    :return: Разобранные данные JSON.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл не найден: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json_file(data: Dict[str, Any], file_path: str) -> None:
    """
    Сохраняет словарь в JSON-файл.

    :param data: Данные для сохранения.
    :param file_path: Путь для сохранения JSON-файла.
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)