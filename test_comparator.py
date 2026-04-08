import pytest
from comparator import compare_lines, save_to_file, get_file_content


@pytest.fixture
def temp_file(tmp_path):
    return tmp_path / "test_file.txt"


@pytest.mark.parametrize("set1, set2, expected_same, expected_diff", [
    ({"a", "b"}, {"b", "c"}, ["b"], ["a", "c"]),
    ({"1"}, {"2"}, [], ["1", "2"]),
    (set(), {"x"}, [], ["x"])
])
def test_compare_logic(set1, set2, expected_same, expected_diff):
    same, diff = compare_lines(set1, set2)
    assert same == expected_same
    assert diff == expected_diff


@pytest.mark.parametrize("file_content, expected_result", [
    ("line1\nline2\nline3", {"line1", "line2", "line3"}),
    ("  line1  \n\nline2  ", {"line1", "line2"}),
    ("", set()),
])
def test_get_file_content_valid(temp_file, file_content, expected_result):
    temp_file.write_text(file_content, encoding='utf-8')
    result = get_file_content(str(temp_file))
    assert result == expected_result


def test_get_file_content_not_found():
    result = get_file_content("non_existent_file.txt")
    assert result == set()


@pytest.mark.parametrize("lines_to_save, expected_file_content", [
    (["a", "b", "c"], "a\nb\nc"),
    ([], ""),
    (["тест"], "тест"),
])
def test_save_to_file(temp_file, lines_to_save, expected_file_content):
    save_to_file(lines_to_save, str(temp_file))
    assert temp_file.read_text(encoding='utf-8') == expected_file_content
