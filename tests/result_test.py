import unittest
from unittest.mock import MagicMock
from result import Result


class TestResult(unittest.TestCase):
    def test_success(self):
        result = Result.of(10)
        mock_on_success = MagicMock(return_value=20)
        mock_on_failure = MagicMock()
        self.assertEqual(result.when(mock_on_success, mock_on_failure), 20)

    def test_failure(self):
        result = Result.failure("Error")
        mock_on_success = MagicMock()
        mock_on_failure = MagicMock(return_value="Handled")
        self.assertEqual(result.when(mock_on_success, mock_on_failure), "Handled")

    def test_repr(self):
        result = Result.of(10)
        self.assertEqual(str(result), "Success: 10")
        result = Result.failure("Error")
        self.assertEqual(str(result), "Error: Error")


if __name__ == "__main__":
    unittest.main()
