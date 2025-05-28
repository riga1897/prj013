from os.path import isfile

from utilities.utilities import get_project_root


def test_get_project_root() -> None:
    """Функция проверяет наличие указанного файла"""
    assert isfile(get_project_root() / "tests" / "test_utilities.py") is True
