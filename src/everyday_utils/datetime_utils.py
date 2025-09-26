from datetime import datetime

def current_datetime(format_str: str = '%Y-%m-%d %H:%M:%S') -> str:
    """
    Получает текущую дату и время в указанном формате.

    :param format_str: Формат строки для даты и времени.
    :return: Отформатированная текущая дата и время.
    """
    return datetime.now().strftime(format_str)