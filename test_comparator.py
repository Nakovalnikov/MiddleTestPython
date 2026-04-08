import pytest
from comparator import compare_lines, save_to_file

@pytest.fixture
def temp_output(tmp_path):
    return tmp_path / "test_result.txt"

@pytest.mark.parametrize("set1, set2, expected_same, expected_diff", [
    ({"a", "b"}, {"b", "c"}, ["b"], ["a", "c"]),
    ({"1"}, {"2"}, [], ["1", "2"]),
    (set(), {"x"}, [], ["x"])
])
def test_compare_logic(set1, set2, expected_same, expected_diff):
    same, diff = compare_lines(set1, set2)
    assert same == expected_same
    assert diff == expected_diff