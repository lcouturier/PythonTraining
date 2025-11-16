from typing import List
import unittest

from lazy import Lazy


class TestLazyHasValue(unittest.TestCase):
    def setUp(self):
        self.lazy_obj = Lazy[str](lambda: "test value")

    def test_has_value_with_value(self):
        self.lazy_obj()
        self.assertTrue(self.lazy_obj.has_value)

    def test_has_value_without_value(self):
        self.lazy_obj = Lazy(lambda: None)
        self.assertFalse(self.lazy_obj.has_value)

    def test_has_value_after_evaluate(self):
        self.lazy_obj()
        self.assertTrue(self.lazy_obj.has_value)

    def test_list_of_int(self):
        self.lazy_obj = Lazy[List[int]](lambda: [1, 2, 3])
        self.assertEqual(self.lazy_obj(), [1, 2, 3])
        self.assertTrue(self.lazy_obj.has_value)
        self.assertTrue(self.lazy_obj.is_evaluted)
        self.assertFalse(self.lazy_obj.is_empty)
        self.assertTrue(self.lazy_obj())
        self.lazy_obj.reset()
        self.assertFalse(self.lazy_obj.has_value)
        self.assertFalse(self.lazy_obj.is_evaluted)
        self.assertTrue(self.lazy_obj.is_empty)
        self.assertTrue(self.lazy_obj())


if __name__ == "__main__":
    unittest.main()
