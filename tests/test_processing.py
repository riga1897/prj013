import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize("test_state", ["EXECUTED", "CANCELED", "UNKNOWN", None, ""])
def test_my_filter_by_state(
    test_filter_input_list,
    test_filtered_by_state_executed,
    test_filtered_by_state_canceled,
    test_state,
    test_state_executed,
    test_state_canceled,
):
    if test_state == test_state_executed:
        assert filter_by_state(test_filter_input_list, test_state) == test_filtered_by_state_executed
    elif (test_state == "") or (not test_state):
        assert filter_by_state(test_filter_input_list) == test_filtered_by_state_executed
    elif test_state == test_state_canceled:
        assert filter_by_state(test_filter_input_list, test_state) == test_filtered_by_state_canceled
    # else:
    #     with pytest.raises(TypeError):
    #         filter_by_state(test_filter_input_list, test_state)


#
#
# @pytest.mark.parametrize("test_import_list", [None, ""])
# def test_my_filter_by_state_null_list(test_filter_input_list, test_import_list):
#     with pytest.raises(TypeError):
#         filter_by_state(test_import_list)


@pytest.mark.parametrize("revers", [True, False, None, "", "Error"])
def test_my_sort_by_date(
    test_filter_input_list,
    revers,
    test_sort_by_date_result_rt,
    test_my_reverse_true,
    test_my_reverse_false,
    test_sort_by_date_result_rf,
):
    if revers == test_my_reverse_false:
        assert sort_by_date(test_filter_input_list, revers) == test_sort_by_date_result_rf
    if revers == test_my_reverse_true:
        assert sort_by_date(test_filter_input_list, revers) == test_sort_by_date_result_rt
    elif (revers == "") or (not revers):
        assert sort_by_date(test_filter_input_list) == test_sort_by_date_result_rt
    else:
        assert sort_by_date(test_filter_input_list, revers) == test_sort_by_date_result_rt
