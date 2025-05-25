from datetime import datetime
from functools import wraps
from pathlib import Path
from typing import Any, Callable

from utilities.utilities import get_project_root

logfile = get_project_root() / "logs" / "mylog.txt"


def log(filename: Path | None) -> Callable:
    """
    Функция содержит декоратор.
    Принимает в качестве аргумента путь к файлу логирования, который будет использоваться декоратором
    """

    def decorator(func: Callable[[*tuple[int | str, ...]], Any]) -> Any:
        """Функция-декоратор. Принимает в качестве аргумента исходную функцию my_function"""

        @wraps(func)
        def wrapper(*args: int | str, **kwargs: Any) -> Any:
            """Функция 'обертка' для приема аргументов исходной функции my_function"""
            to_log = ""
            start_time = datetime.now().strftime("%d-%b-%Y %H:%M:%S.%f")
            to_log += f"{func.__name__} started: {start_time}\n"
            try:
                result = func(*args, **kwargs)
            except Exception as error_info:
                err_type = type(error_info).__name__
                to_log += f"{func.__name__} error: {err_type}. Inputs: ({args}), {kwargs}\n"
                result = f"Error, {error_info}"
                return result
            else:
                to_log += f"{func.__name__} ok\n"
                print(result)
                return result
            finally:
                end_time = datetime.now().strftime("%d-%b-%Y %H:%M:%S.%f")
                to_log += f"{func.__name__} stoped: {end_time}\n"
                if not filename:
                    print(to_log)
                else:
                    with open(filename, "a") as file:
                        file.write(to_log)

        return wrapper

    return decorator


@log(filename=logfile)
def my_function(x: int, y: int) -> int:
    """Функция принимает в качестве аргументов два значения и возвращает их сумму"""
    return x + y


# if __name__ == "__main__":
#     my_function(2, 4)
