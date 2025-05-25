from typing import List


def filter_by_state(my_list: List, my_state: str = "EXECUTED") -> List | None:
    """
    Функция фильтрует исходный список по значению параметра 'state'.
    Если параметр не задан, то фильтрация по значению 'EXECUTED'
    """
    is_list = isinstance(my_list, list)
    result = []
    if is_list:
        # try:
        filtered_list = [item for item in my_list if item.get("state", {}) == my_state]
        # except TypeError:
        #     raise TypeError("Неверный формат даты")
        # else:
        # if not len(filtered_list) > 0:
        #     raise TypeError("Нет данных")
        # else:
        result = filtered_list
    return result


def sort_by_date(my_list: List, descending: bool = True) -> List:
    """
    Функция сортирует исходный список по значению параметра 'date'
    Направление сортировки задается параметром 'descending'
    Если значение параметра True или параметр не задан, то сортировка по убыванию.
    Если задан параметр False, то сортировка по возрастанию.
    """
    result = sorted(my_list, key=lambda my_item: my_item.get("date"), reverse=descending)

    return result


# if __name__ == "__main__":
#    input_list = [
#        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#    ]
#
#    print(filter_by_state(input_list))
#    print(sort_by_date(input_list))
