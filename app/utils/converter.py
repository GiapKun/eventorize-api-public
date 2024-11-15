import time
from datetime import datetime

from utils import value


def convert_datetime_to_str(datetime_obj: datetime) -> str:
    """
    Converts a datetime object to a string using the format "%Y-%m-%d %H:%M:%S".

    Args:
        datetime_obj (datetime): The datetime object to be converted to a string.

    Returns:
        formatted_datetime (str): The datetime object as a formatted string in the format "%Y-%m-%d %H:%M:%S".
    """
    return datetime_obj.strftime(value.DataFormat.DATE_TIME.value)


def convert_str_to_datetime(datetime_str: str) -> datetime:
    """
    Converts a datetime string in the format "%Y-%m-%d %H:%M:%S" to a datetime object.

    Args:
        datetime_str (str): The datetime string to be converted.

    Returns:
        datetime_obj (datetime): The corresponding datetime object.

    """
    return datetime.strptime(datetime_str, value.DataFormat.DATE_TIME.value)


def convert_str_to_datetime_by_format(datetime_str: str, date_format=r"%Y-%m-%d") -> datetime:
    """
    Converts a datetime string in the format "%Y-%m-%d %H:%M:%S" to a datetime object.

    Args:
        datetime_str (str): The datetime string to be converted.

    Returns:
        datetime_obj (datetime): The corresponding datetime object.

    """
    return datetime.strptime(datetime_str, date_format)


def convert_date_string_to_timestamp(datetime_str: str, date_format=r"%Y-%m-%d"):
    """
    Convert a date string in the format 'YYYY-MM-DD' to a Unix timestamp.

    Args:
        date (str): A date string in the format 'YYYY-MM-DD'.

    Returns:
        float: The Unix timestamp representation of the input date.

    Example:
        >>> Converter.convert_date_string_to_timestamp('2024-07-02')
        1725168000.0
    """
    return time.mktime(datetime.strptime(datetime_str, date_format).timetuple())
