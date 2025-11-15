import unittest

from compteur import Compteur


class MyTestCase(unittest.TestCase):
    def test_something(self):
        c = Compteur(10)
        c += 5
        self.assertEqual(c.value, 15)  # add assertion here
        self.assertEqual(c.__repr__(), 'Compteur(15)')  # add assertion here
        c -= 3
        self.assertEqual(c.value, 12)  # add assertion here


if __name__ == '__main__':
    unittest.main()
