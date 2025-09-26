import hashlib

def hash_string(input_str: str, algorithm: str = 'sha256') -> str:
    """
    Хеширует строку с использованием указанного алгоритма (например, 'md5', 'sha256').

    :param input_str: Строка для хеширования.
    :param algorithm: Алгоритм хеширования.
    :return: Шестнадцатеричный дайджест хеша.
    """
    if not isinstance(input_str, str):
        raise TypeError("input_str должен быть строкой.")
    hasher = hashlib.new(algorithm)
    hasher.update(input_str.encode('utf-8'))
    return hasher.hexdigest()