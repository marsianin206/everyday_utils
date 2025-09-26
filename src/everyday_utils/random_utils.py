import random
from typing import List, Any, Dict

def random_choice_from_list(items: List[Any]) -> Any:
    """
    Выбирает случайный элемент из списка.

    :param items: Список элементов.
    :return: Случайно выбранный элемент.
    """
    if not items:
        raise ValueError("Список не может быть пустым.")
    return random.choice(items)

def flatten_list(nested_list: List[Any]) -> List[Any]:
    """
    Преобразует вложенный список в одноуровневый.

    :param nested_list: Вложенный список.
    :return: Плоский список.
    """
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

def unique_list(items: List[Any]) -> List[Any]:
    """
    Удаляет дубликаты из списка, сохраняя порядок.

    :param items: Список для обработки.
    :return: Список с уникальными элементами.
    """
    seen = set()
    return [x for x in items if not (x in seen or seen.add(x))]

def deep_merge_dicts(dict1: Dict[Any, Any], dict2: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Глубоко объединяет два словаря, рекурсивно сливая вложенные словари.

    :param dict1: Первый словарь.
    :param dict2: Второй словарь (перезаписывает dict1 при конфликтах).
    :return: Объединенный словарь.
    """
    result = dict1.copy()
    for key, value in dict2.items():
        if isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = deep_merge_dicts(result[key], value)
        else:
            result[key] = value
    return result

def mean(numbers: List[float]) -> float:
    """
    Вычисляет среднее значение списка чисел.

    :param numbers: Список чисел.
    :return: Среднее значение.
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def median(numbers: List[float]) -> float:
    """
    Вычисляет медиану списка чисел.

    :param numbers: Список чисел (будет отсортирован).
    :return: Медианное значение.
    """
    if not numbers:
        return 0.0
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    if n % 2 == 0:
        return (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
    return sorted_nums[n//2]