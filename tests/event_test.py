import pytest

from even import load_even_number_from_csv_file, get_even_number_first_version


def test_load_even_number_from_csv_file_reads_only_evens(tmp_path):
    csv_content = "2\n3\n4\n5\n6\n-2\n"
    test_file = tmp_path / "numbers.csv"
    test_file.write_text(csv_content, encoding="utf-8")

    result = load_even_number_from_csv_file(str(test_file))
    assert result == [2, 4, 6, -2]  # Excludes odd numbers, includes negative even


def test_load_even_number_from_csv_file_empty_file(tmp_path):
    test_file = tmp_path / "empty.csv"
    test_file.write_text("", encoding="utf-8")
    assert load_even_number_from_csv_file(str(test_file)) == []


def test_load_even_number_from_csv_file_handles_invalid_lines(tmp_path):
    # Test file with some non-integer lines should raise ValueError
    csv_content = "2\nfoo\n4\n"
    test_file = tmp_path / "invalid.csv"
    test_file.write_text(csv_content, encoding="utf-8")

    with pytest.raises(ValueError):
        load_even_number_from_csv_file(str(test_file))


@pytest.mark.parametrize(
    "start, stop, step, expected",
    [
        (0, 10, 1, [0, 2, 4, 6, 8]),
        (1, 9, 2, [2, 4, 6, 8]),
        (2, 2, 1, []),
        (0, 1, 1, [0]),
        (-6, 1, 2, [-6, -4, -2, 0]),
        (5, 16, 3, [6, 12]),
        (0, -5, -1, [0, -2, -4]),
    ],
)
def test_get_even_number_first_version_various_cases(start, stop, step, expected):
    assert get_even_number_first_version(start, stop, step) == expected


def test_get_even_number_first_version_step_zero_raises():
    with pytest.raises(ValueError):
        # range() with step=0 raises ValueError
        get_even_number_first_version(0, 10, 0)
