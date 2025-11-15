import unittest
import factorial




class MyTestCase(unittest.TestCase):
    def test_another_factorial(self):
        (duration, result) = factorial.another_factorial(4)
        print(duration)
        self.assertEqual(result, [1, 1, 2, 6, 24])

    def test_factorial_bottom_up(self):
        f = factorial.factorial_bottom_up()
        result = f(4)
        self.assertEqual(result, 24)

    def test_factorial_by_acc(self):
        result = factorial.factorial_by_acc(10)
        self.assertEqual(result, 3628800)
    


if __name__ == '__main__':
    unittest.main()
