from src.decorators import log, my_function
from src.utils import get_project_root


def test_log_good() -> None:
    my_function(5, 7)
    with open(get_project_root() / "logs" / "mylog.txt", "r") as file:
        status = file.readlines()[-2]
        assert status == "my_function ok\n"


def test_log_bad() -> None:
    my_function(5, "7")
    with open(get_project_root() / "logs" / "mylog.txt", "r") as file:
        status = file.readlines()[-2]
        assert status == "my_function error: TypeError. Inputs: ((5, '7')), {}\n"


@log(filename=None)
def test_log_null_good(capsys):
    my_function(7, 9)
    captured = capsys.readouterr()
    assert captured.out.strip() == "16"


@log(filename=None)
def test_log_null_bad(capsys):
    my_function(7, "9")
    captured = capsys.readouterr()
    assert captured.out.strip() == ""


def test_my_function() -> None:
    assert my_function.__wrapped__(5, 7) == 12
