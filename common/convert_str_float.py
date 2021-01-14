from typing import Optional, Union


def convert_str_float(val:str) -> Optional[Union[float, str]]:
    """Checks if passed value is string which can be typecast to float, if val is empty returns None

    Args:
        val (str): The value to check

    Returns:
        Optional[Union[float, str]]: If val does not exist, returns None. Otherwise val or float(val).
    """
    if not val:
        return None
    try:
        return float(val)
    except ValueError:
        return val