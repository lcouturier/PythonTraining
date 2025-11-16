import unittest

from lazy import Lazy


class TestLazyHasValue(unittest.TestCase):
    def setUp(self):
        self.lazy_obj = Lazy(lambda: "test value")

    def test_has_value_with_value(self):
        self.lazy_obj()
        self.assertTrue(self.lazy_obj.has_value)

    def test_has_value_without_value(self):
        self.lazy_obj = Lazy(lambda: None)
        self.assertFalse(self.lazy_obj.has_value)

    def test_has_value_after_evaluate(self):
        self.lazy_obj()
        self.assertTrue(self.lazy_obj.has_value)


if __name__ == "__main__":
    unittest.main()
