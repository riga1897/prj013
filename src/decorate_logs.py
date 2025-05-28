import logging
from functools import wraps
from typing import Any, Callable


def logged(module_name: str = "decorate_logs") -> Callable:
    """
    Функция содержит декоратор.
    Принимает в качестве аргумента путь к файлу логирования, который будет использоваться декоратором
    """

    logger = logging.getLogger(module_name)
    logger.setLevel(logging.DEBUG)

    def decorator(func: Callable | Any) -> Any:
        """Функция-декоратор. Принимает в качестве аргумента исходную функцию my_function"""

        @wraps(func)
        def wrapper(*args: int | str, **kwargs: Any) -> Any:
            """Функция 'обертка' для приема аргументов исходной функции my_function"""

            try:
                logger.info(f'Executing function: "{func.__name__}".')
                result = func(*args, **kwargs)
            except Exception as error_info:
                err_type = type(error_info).__name__
                result = f"Error, {error_info}"
                logger.error(f'Function: "{func.__name__}" error: {err_type}, {error_info}.')
                return result
            else:
                logger.info(f'Function: "{func.__name__}" ok.')  # , result: ({result}).')
                return result
            finally:
                logger.info(f'Stoped function: "{func.__name__}".')

        return wrapper

    return decorator


# if __name__ == "__main__":
#     print()
