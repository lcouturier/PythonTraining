import unittest
from unittest.mock import patch
from io import StringIO
from annotations import log


class TestLogDecorator(unittest.TestCase):
    def test_log_with_positional_args(self):
        """Test that log decorator prints function call with positional arguments"""

        @log
        def add(a, b):
            return a + b

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            result = add(3, 4)
            output = mock_stdout.getvalue()

        self.assertEqual(result, 7)
        self.assertIn("Calling add with args=(3, 4) and kwargs={}", output)
        self.assertIn("add returned 7", output)

    def test_log_with_keyword_args(self):
        """Test that log decorator prints function call with keyword arguments"""

        @log
        def multiply(x, y):
            return x * y

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            result = multiply(x=5, y=6)
            output = mock_stdout.getvalue()

        self.assertEqual(result, 30)
        self.assertIn(
            "Calling multiply with args=() and kwargs={'x': 5, 'y': 6}", output
        )
        self.assertIn("multiply returned 30", output)

    def test_log_with_mixed_args(self):
        """Test that log decorator prints function call with mixed arguments"""

        @log
        def greet(name, greeting="Hello"):
            return f"{greeting}, {name}!"

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            result = greet("Alice", greeting="Hi")
            output = mock_stdout.getvalue()

        self.assertEqual(result, "Hi, Alice!")
        self.assertIn(
            "Calling greet with args=('Alice',) and kwargs={'greeting': 'Hi'}", output
        )
        self.assertIn("greet returned Hi, Alice!", output)

    def test_log_with_no_args(self):
        """Test that log decorator works with functions that take no arguments"""

        @log
        def get_constant():
            return 42

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            result = get_constant()
            output = mock_stdout.getvalue()

        self.assertEqual(result, 42)
        self.assertIn("Calling get_constant with args=() and kwargs={}", output)
        self.assertIn("get_constant returned 42", output)

    def test_log_preserves_function_name(self):
        """Test that log decorator preserves the original function name"""

        @log
        def test_function():
            return "test"

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            test_function()
            output = mock_stdout.getvalue()

        self.assertIn("test_function", output)

    def test_log_with_none_return_value(self):
        """Test that log decorator handles None return values"""

        @log
        def return_none():
            return None

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            result = return_none()
            output = mock_stdout.getvalue()

        self.assertIsNone(result)
        self.assertIn("return_none returned None", output)


if __name__ == "__main__":
    unittest.main()
