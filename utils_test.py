import unittest

from utils import unfold


class MyTestCase(unittest.TestCase):
    def test_unfold(self):
        generator = unfold(1, lambda x: x + 2)
        result = [next(generator) for _ in range(10)]

        print(result)
        self.assertEqual(result, [1, 3, 5, 7, 9, 11, 13, 15, 17, 19])


if __name__ == '__main__':
    unittest.main()
